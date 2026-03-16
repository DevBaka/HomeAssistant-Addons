"""Sensor platform for DOCSight integration."""
import asyncio
import logging
from datetime import datetime
from typing import Dict, Any

import aiohttp
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, SENSOR_STATUS, SENSOR_UPTIME, SENSOR_LAST_CHECK

_LOGGER = logging.getLogger(__name__)

class DOCSightCoordinator(DataUpdateCoordinator):
    """Data coordinator for DOCSight."""

    def __init__(self, hass: HomeAssistant, host: str, port: int) -> None:
        """Initialize coordinator."""
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=30,  # Update every 30 seconds
        )

    async def _async_update_data(self) -> Dict[str, Any]:
        """Update data via API."""
        try:
            async with aiohttp.ClientSession() as session:
                # Get health status
                async with session.get(f"{self.base_url}/health", timeout=5) as response:
                    if response.status == 200:
                        status = "Online"
                    else:
                        status = "Error"
                
                # Get additional stats if available
                try:
                    async with session.get(f"{self.base_url}/api/status", timeout=5) as response:
                        if response.status == 200:
                            data = await response.json()
                            return {
                                "status": status,
                                "uptime": data.get("uptime", "Unknown"),
                                "last_check": data.get("last_check", datetime.now().isoformat()),
                                "issues_detected": data.get("issues_detected", 0),
                            }
                except Exception:
                    pass
                
                return {
                    "status": status,
                    "uptime": "Unknown",
                    "last_check": datetime.now().isoformat(),
                    "issues_detected": 0,
                }
        except Exception as error:
            raise UpdateFailed(f"Error communicating with DOCSight: {error}")

class DOCSightSensor(SensorEntity):
    """Base class for DOCSight sensors."""

    def __init__(self, coordinator: DOCSightCoordinator, sensor_name: str) -> None:
        """Initialize sensor."""
        self.coordinator = coordinator
        self._sensor_name = sensor_name
        self._attr_name = f"DOCSight {sensor_name.replace('_', ' ').title()}"
        self._attr_unique_id = f"{DOMAIN}_{sensor_name}"
        self._attr_should_poll = False

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self) -> None:
        """Update entity."""
        await self.coordinator.async_request_refresh()

class DOCSightStatusSensor(DOCSightSensor):
    """Sensor for DOCSight status."""

    def __init__(self, coordinator: DOCSightCoordinator) -> None:
        super().__init__(coordinator, "status")
        self._attr_icon = "mdi:network-outline"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def state(self) -> str:
        """Return the sensor state."""
        return self.coordinator.data.get("status", "Unknown")

class DOCSightUptimeSensor(DOCSightSensor):
    """Sensor for DOCSight uptime."""

    def __init__(self, coordinator: DOCSightCoordinator) -> None:
        super().__init__(coordinator, "uptime")
        self._attr_icon = "mdi:clock-outline"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def state(self) -> str:
        """Return the sensor state."""
        return self.coordinator.data.get("uptime", "Unknown")

class DOCSightLastCheckSensor(DOCSightSensor):
    """Sensor for last check time."""

    def __init__(self, coordinator: DOCSightCoordinator) -> None:
        super().__init__(coordinator, "last_check")
        self._attr_icon = "mdi:update"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_device_class = SensorDeviceClass.TIMESTAMP

    @property
    def state(self) -> str:
        """Return the sensor state."""
        return self.coordinator.data.get("last_check")

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up DOCSight sensors."""
    host = entry.data["host"]
    port = entry.data["port"]
    
    coordinator = DOCSightCoordinator(hass, host, port)
    
    # Initial refresh
    await coordinator.async_config_entry_first_refresh()
    
    entities = [
        DOCSightStatusSensor(coordinator),
        DOCSightUptimeSensor(coordinator),
        DOCSightLastCheckSensor(coordinator),
    ]
    
    async_add_entities(entities)
