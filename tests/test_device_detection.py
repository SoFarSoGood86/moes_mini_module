from custom_components.moes_mini_module.config_flow import detect_device_type_from_dps

def test_detect_dimmer():
    assert detect_device_type_from_dps({'1': True, '2': 85}) == 'dimmer_1'

def test_detect_switch3():
    assert detect_device_type_from_dps({'1':'a','2':'b','3':'c'}) == 'switch_3'

def test_detect_curtain():
    assert detect_device_type_from_dps({'1':True,'101':50}) == 'curtain'
