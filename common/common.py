import logging
import json

LOGFILENAME = 'anywhere.log'

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename=LOGFILENAME,
    filemode='w')

logger = logging.getLogger(__name__)

def load_config(configfile):
    with open(configfile) as json_conf_file:
        config = json.load(json_conf_file)
    return config