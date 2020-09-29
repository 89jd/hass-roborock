"""Support for Xiaomi Miio."""
import logging

from homeassistant import config_entries, core

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: core.HomeAssistant, config: dict):
    return True


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
):
    hass.async_add_job(hass.config_entries.async_forward_entry_setup(entry, "vacuum"))

    return True
