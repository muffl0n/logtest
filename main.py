import logging
import logging.config
from pathlib import Path


def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger = logging.LoggerAdapter(logger, {})

    path = Path('/tmp')

    for entry in path.iterdir():
        logger.extra = {'entry': entry.name}
        logger.info(entry.stat().st_size)

    logger = logging.getLogger('test')
    logger = logging.LoggerAdapter(logger, {'entry': 'n/a'})
    logger.warning('testwarning')
    logger.error('testerror')

if __name__ == '__main__':
    main()
