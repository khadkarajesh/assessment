import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format = '%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(filename="app.log", format=log_format,
                    datefmt='%Y-%m-%d %H:%M:%S')
