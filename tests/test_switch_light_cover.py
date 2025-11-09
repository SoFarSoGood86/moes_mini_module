from custom_components.moes_mini_module.device import MoesDevice
from custom_components.moes_mini_module.switch import MoesSwitch
from custom_components.moes_mini_module.light import MoesDimmerLight
from custom_components.moes_mini_module.cover import MoesCover

def test_switch_calls_set_dps(monkeypatch):
    dev = MoesDevice('id','ip','key')
    s = MoesSwitch(dev, 'sw', 1)
    s.turn_on()
    s.turn_off()

def test_light_calls_set_dps():
    dev = MoesDevice('id','ip','key')
    l = MoesDimmerLight(dev, 'light')
    l.turn_on(brightness=128)
    l.turn_off()

def test_cover_methods():
    dev = MoesDevice('id','ip','key')
    c = MoesCover(dev, 'cover')
    c.open_cover()
    c.close_cover()
    c.stop_cover()
    c.set_cover_position(position=50)
