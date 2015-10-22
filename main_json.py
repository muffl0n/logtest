import json
import logging.config

with open('logging.json', 'r') as f:
    config = json.load(f)

logging.config.dictConfig(config)

log = logging.getLogger(__name__)
log.info('test')

log = logging.getLogger('test')
log.info('test')
