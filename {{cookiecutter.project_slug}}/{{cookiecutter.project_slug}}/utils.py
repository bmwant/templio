import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(fmt=logging.Formatter(fmt=logging.BASIC_FORMAT))
logger.addHandler(handler)
