import logging
from homeassistant.components.light import LightEntity, SUPPORT_BRIGHTNESS
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
    device_type = data.get("device_type", "dimmer_1")

    device = MoesDevice(device_id, ip, local_key)
    entities = []
    if device_type == "dimmer_1":
        entities.append(MoesDimmerLight(device, name + " (Dimmer 1)"))
    elif device_type == "dimmer_2":
        entities.append(MoesDimmerLight(device, name + " (Dimmer 1)"))
        entities.append(MoesDimmerLight(device, name + " (Dimmer 2)"))
    async_add_entities(entities)

class MoesDimmerLight(LightEntity):
    def __init__(self, device: MoesDevice, name: str):
        self._device = device
        self._name = name
        self._is_on = False
        self._brightness = 0

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def brightness(self):
        return int(self._brightness * 255 / 100)

    @property
    def supported_features(self):
        return SUPPORT_BRIGHTNESS

    def turn_on(self, **kwargs):
        brightness = kwargs.get("brightness")
        try:
            if brightness is not None:
                b = int(brightness * 100 / 255)
                self._device.set_dps(2, b)
                self._brightness = b
                self._is_on = b > 0
            else:
                self._device.turn_on()
                self._is_on = True
        except Exception as e:
            _LOGGER.exception("Failed to turn_on: %s", e)

    def turn_off(self, **kwargs):
        try:
            self._device.set_dps(1, False)
            self._is_on = False
        except Exception as e:
            _LOGGER.exception("Failed to turn_off: %s", e)

    def update(self):
        data = self._device.status()
        dps = data.get("dps", {})
        if '1' in dps:
            self._is_on = bool(dps.get('1'))
        if '2' in dps:
            try:
                self._brightness = int(dps.get('2') or 0)
            except Exception:
                self._brightness = 0
