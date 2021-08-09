from logging import Logger


def add(a: int, b: int, *, logger: Logger) -> int:
    res: int = a + b

    # logging with module logger
    logger = logger
    logger.debug(f"result: {res}")
    return res
