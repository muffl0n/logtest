import json
import logging.config
import yaml

with open('logging.yaml', 'r') as f:
    config = yaml.load(f)

logging.config.dictConfig(config)

log = logging.getLogger(__name__)
log.info('test')
