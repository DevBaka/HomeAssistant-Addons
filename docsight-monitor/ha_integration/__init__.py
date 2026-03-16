"""DOCSight integration for Home Assistant."""
import asyncio
import logging
from typing import Dict, Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_URL, CONF_PORT

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the DOCSight integration."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up DOCSight from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    # Register frontend panel
    hass.components.frontend.async_register_built_in_panel(
        "iframe",
        "DOCSight",
        "mdi:network-outline",
        {
            "title": "DOCSight",
            "icon": "mdi:network-outline",
            "url": f"http://{hass.config.api.host}:{entry.data.get(CONF_PORT, 8765)}",
            "require_admin": False,
        },
    )
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
