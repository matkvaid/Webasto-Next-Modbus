import logging
from homeassistant.helpers import discovery
from homeassistant.components import modbus

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up Modbus integration"""
    modbus_config = config.get('modbus', {})
    
    if not modbus_config:
        _LOGGER.error("Modbus configuration is required")
        return False
        
    # Initialize Modbus connection
    modbus.setup(hass, modbus_config)
    
    _LOGGER.info("Modbus integration initialized")
    return True
