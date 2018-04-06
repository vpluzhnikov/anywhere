from common.common import logger, load_config
import logging

# Loads configurations and performs postproccessing fo anywhere config file
#


class anywhere_config:

    def __init__(self, configfile):
        self.logger = logging.getLogger(__name__)
        self.config = load_config(configfile)
        self.valid = True

        if self.config:
            try:
                if 'providers' in self.config.keys():
                    for provider in self.config['providers']:
                        logger.log(provider)
                else:
                    logger.error('No providers are found in config file')
                    self.valid = False
            except:
                self.logger.error('Error loading configuration from ' + configfile)
                self.valid = False
