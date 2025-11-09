import logging
from homeassistant.components.cover import CoverEntity, SUPPORT_OPEN, SUPPORT_CLOSE, SUPPORT_STOP, SUPPORT_SET_POSITION
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
    device_type = data.get("device_type", "curtain")

    device = MoesDevice(device_id, ip, local_key)
    entities = []
    if device_type in ["curtain", "garage"]:
        entities.append(MoesCover(device, name))
    async_add_entities(entities)

class MoesCover(CoverEntity):
    def __init__(self, device: MoesDevice, name: str):
        self._device = device
        self._name = name
        self._position = None
        self._is_open = False

    @property
    def name(self):
        return self._name

    @property
    def supported_features(self):
        return SUPPORT_OPEN | SUPPORT_CLOSE | SUPPORT_STOP | SUPPORT_SET_POSITION

    def open_cover(self, **kwargs):
        try:
            self._device.set_dps(1, True)
        except Exception as e:
            _LOGGER.exception("Failed to open cover: %s", e)

    def close_cover(self, **kwargs):
        try:
            self._device.set_dps(2, True)
        except Exception as e:
            _LOGGER.exception("Failed to close cover: %s", e)

    def stop_cover(self, **kwargs):
        try:
            self._device.set_dps(3, True)
        except Exception as e:
            _LOGGER.exception("Failed to stop cover: %s", e)

    def set_cover_position(self, **kwargs):
        position = kwargs.get('position')
        if position is None:
            return
        try:
            self._device.set_dps(101, int(position))
            self._position = int(position)
        except Exception as e:
            _LOGGER.exception("Failed to set cover position: %s", e)

    def update(self):
        data = self._device.status()
        dps = data.get('dps', {})
        if '101' in dps:
            try:
                self._position = int(dps.get('101') or 0)
            except Exception:
                self._position = None
        if '1' in dps and '2' in dps:
            self._is_open = bool(dps.get('1')) and not bool(dps.get('2'))
