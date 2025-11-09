import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_tinytuya(monkeypatch):
    class MockDevice:
        def __init__(self, *a, **kw): pass
        def set_version(self, v): pass
        def status(self):
            return {'dps': {'1': True, '2': 50}}
        def set_value(self, dps, value):
            return {str(dps): value}
        def turn_on(self): return True
        def turn_off(self): return True
    monkeypatch.setattr('custom_components.moes_mini_module.device.tinytuya.OutletDevice', MockDevice)
