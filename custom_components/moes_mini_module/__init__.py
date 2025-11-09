from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass, entry):
    await hass.config_entries.async_forward_entry_setups(entry, ["light", "switch", "cover"])
    hass.data[DOMAIN][entry.entry_id] = entry
    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_unload_platforms(entry, ["light", "switch", "cover"])
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
