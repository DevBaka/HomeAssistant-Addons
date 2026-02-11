"""Config flow for DOCSight integration."""
import logging
from typing import Dict, Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN, DEFAULT_PORT

_LOGGER = logging.getLogger(__name__)

class DOCSightConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for DOCSight."""

    VERSION = 1

    async def async_step_user(
        self, user_input: Dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: Dict[str, str] = {}

        if user_input is not None:
            # Validate connection
            host = user_input[CONF_HOST]
            port = user_input[CONF_PORT]
            
            # Test connection to DOCSight
            try:
                import aiohttp
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"http://{host}:{port}/health", timeout=5) as response:
                        if response.status == 200:
                            return self.async_create_entry(
                                title="DOCSight",
                                data={
                                    CONF_HOST: host,
                                    CONF_PORT: port,
                                    "url": f"http://{host}:{port}"
                                }
                            )
                        else:
                            errors["base"] = "cannot_connect"
            except Exception:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST, default="homeassistant.local"): str,
                vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
            }),
            errors=errors,
        )
