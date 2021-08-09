import logging


def add(a: int, b: int) -> int:
    res: int = a + b

    # logging with global logger
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"result: {res}")
    return res
