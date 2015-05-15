import logging
import logging.config
from pathlib import Path

def main():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger = logging.LoggerAdapter(logger, {})

    path = Path('/tmp')
    entries = list(path.glob('*'))

    for entry in entries:
        logger.extra = {'entry': entry.name}
        logger.info(entry.stat().st_size)

if __name__ == '__main__':
    main()
