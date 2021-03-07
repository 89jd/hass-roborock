"""Code to handle a Xiaomi Device."""
import logging

from miio import Device, DeviceException

from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import Entity

from .const import CONF_MODEL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class XiaomiMiioEntity(Entity):
    """Representation of a base Xiaomi Miio Entity."""

    def __init__(self, name, device, entry, unique_id):
        """Initialize the Xiaomi Miio Device."""
        self._device = device
        self._model = entry.data[CONF_MODEL]
        self._device_id = entry.unique_id
        self._unique_id = unique_id
        self._name = name

    @property
    def unique_id(self):
        """Return an unique ID."""
        return self._unique_id

    @property
    def name(self):
        """Return the name of this entity, if any."""
        return self._name

    @property
    def device_info(self):
        """Return the device info."""
        device_info = {
            "identifiers": {(DOMAIN, self._device_id)},
            "manufacturer": "Roborock",
            "name": self._name,
            "model": self._model,
        }

        return device_info
