import logging


logging.basicConfig(
    format="%(asctime)s %(levelname)s[%(filename)s:%(funcName)20s() ] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
