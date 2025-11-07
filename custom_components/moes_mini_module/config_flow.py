from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_DEVICE_ID, CONF_LOCAL_KEY, CONF_IP_ADDRESS, CONF_NAME, DEVICE_TYPES

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_IP_ADDRESS): str,
    vol.Required(CONF_DEVICE_ID): str,
    vol.Required(CONF_LOCAL_KEY): str,
    vol.Required("device_type", default="dimmer_1"): vol.In(DEVICE_TYPES),
    vol.Optional(CONF_NAME): str,
})

class MoesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is None:
            schema = vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Required(CONF_DEVICE_ID): str,
                vol.Required(CONF_LOCAL_KEY): str,
                vol.Required("device_type", default="dimmer_1"): vol.In(DEVICE_TYPES),
                vol.Optional(CONF_NAME): str,
            })
            return self.async_show_form(step_id="user", data_schema=schema)

        return self.async_create_entry(title=user_input.get(CONF_NAME) or user_input[CONF_DEVICE_ID], data=user_input)
