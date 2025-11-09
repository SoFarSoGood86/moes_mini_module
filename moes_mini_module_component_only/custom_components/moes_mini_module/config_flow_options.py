from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

OPTIONS_SCHEMA = vol.Schema({
    vol.Optional('dp_on_off', default=1): int,
    vol.Optional('dp_brightness', default=2): int,
    vol.Optional('dp_stop', default=3): int,
    vol.Optional('dp_position', default=101): int,
})

class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is None:
            return self.async_show_form(step_id='init', data_schema=OPTIONS_SCHEMA)
        return self.async_create_entry(title='', data=user_input)
