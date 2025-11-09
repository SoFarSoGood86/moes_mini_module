from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, CONF_DEVICE_ID, CONF_LOCAL_KEY, CONF_IP_ADDRESS, CONF_NAME, DEVICE_TYPES
from .device import MoesDevice
import logging

_LOGGER = logging.getLogger(__name__)

STEP_USER_SCHEMA = vol.Schema({
    vol.Required(CONF_IP_ADDRESS): str,
    vol.Required(CONF_DEVICE_ID): str,
    vol.Required(CONF_LOCAL_KEY): str,
    vol.Optional(CONF_NAME): str,
})

def detect_device_type_from_dps(dps: dict) -> str:
    keys = set(dps.keys())
    if '101' in keys:
        return 'curtain'
    if any(k in keys for k in ['2']) and '1' in keys and not any(k in keys for k in ['3','4']):
        return 'dimmer_1'
    sw_count = sum(1 for k in keys if k.isdigit() and 1 <= int(k) <= 4)
    if sw_count >= 4:
        return 'switch_4'
    if sw_count == 3:
        return 'switch_3'
    if sw_count == 2:
        return 'switch_2'
    if sw_count == 1:
        return 'switch_1'
    return 'switch_1'

class MoesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(step_id='user', data_schema=STEP_USER_SCHEMA)

        try:
            device = MoesDevice(user_input[CONF_DEVICE_ID], user_input[CONF_IP_ADDRESS], user_input[CONF_LOCAL_KEY])
            status = device.status()
            dps = status.get('dps', {})
            detected = detect_device_type_from_dps(dps)
            _LOGGER.debug("DPS détectés: %s -> type détecté: %s", dps, detected)
        except Exception as e:
            _LOGGER.debug("Détection automatique échouée: %s", e)
            detected = 'dimmer_1'

        entry_data = {
            CONF_IP_ADDRESS: user_input[CONF_IP_ADDRESS],
            CONF_DEVICE_ID: user_input[CONF_DEVICE_ID],
            CONF_LOCAL_KEY: user_input[CONF_LOCAL_KEY],
            CONF_NAME: user_input.get(CONF_NAME),
            'device_type': detected
        }
        return self.async_create_entry(title=user_input.get(CONF_NAME) or user_input[CONF_DEVICE_ID], data=entry_data)
