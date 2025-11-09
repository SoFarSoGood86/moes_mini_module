import logging
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import CONF_DEVICE_ID, CONF_LOCAL_KEY, CONF_IP_ADDRESS, CONF_NAME, DEFAULT_NAME
from .device import MoesDevice

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    data = entry.data
    ip = data[CONF_IP_ADDRESS]
    device_id = data[CONF_DEVICE_ID]
    local_key = data[CONF_LOCAL_KEY]
    name = data.get(CONF_NAME, DEFAULT_NAME)
    device_type = data.get("device_type", "switch_1")

    device = MoesDevice(device_id, ip, local_key)
    entities = []
    if device_type.startswith("switch_"):
        try:
            gangs = int(device_type.split("_")[1])
        except Exception:
            gangs = 1
        for i in range(1, gangs+1):
            entities.append(MoesSwitch(device, f"{name} (Switch {i})", i))
    async_add_entities(entities)

class MoesSwitch(SwitchEntity):
    def __init__(self, device: MoesDevice, name: str, index: int):
        self._device = device
        self._name = name
        self._index = index
        self._is_on = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self, **kwargs):
        try:
            self._device.set_dps(self._index, True)
            self._is_on = True
        except Exception as e:
            _LOGGER.exception("Failed to turn_on switch %s: %s", self._index, e)

    def turn_off(self, **kwargs):
        try:
            self._device.set_dps(self._index, False)
            self._is_on = False
        except Exception as e:
            _LOGGER.exception("Failed to turn_off switch %s: %s", self._index, e)

    def update(self):
        data = self._device.status()
        dps = data.get("dps", {})
        key = str(self._index)
        if key in dps:
            self._is_on = bool(dps.get(key))
