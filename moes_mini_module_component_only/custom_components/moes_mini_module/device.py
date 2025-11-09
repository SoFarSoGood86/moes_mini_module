import logging
import tinytuya

_LOGGER = logging.getLogger(__name__)

class MoesDevice:
    def __init__(self, device_id: str, ip: str, local_key: str, version: float = 3.3):
        self.device_id = device_id
        self.ip = ip
        self.local_key = local_key
        self._device = tinytuya.OutletDevice(device_id, ip, local_key)
        try:
            self._device.set_version(version)
        except Exception:
            pass

    def status(self):
        try:
            return self._device.status()
        except Exception as e:
            _LOGGER.debug("tinytuya status() failed: %s", e)
            return {}

    def set_dps(self, dps: int, value):
        try:
            return self._device.set_value(dps, value)
        except Exception as e:
            _LOGGER.exception("set_dps failed: %s", e)
            raise

    def turn_on(self):
        try:
            return self._device.turn_on()
        except Exception as e:
            _LOGGER.exception("turn_on failed: %s", e)
            raise

    def turn_off(self):
        try:
            return self._device.turn_off()
        except Exception as e:
            _LOGGER.exception("turn_off failed: %s", e)
            raise
