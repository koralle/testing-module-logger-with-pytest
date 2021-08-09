from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger


def create_module_logger(
    logger_name: str = __name__, logging_propagate: bool = False
) -> Logger:

    logger = getLogger(logger_name)
    handler = StreamHandler()
    log_format = Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(log_format)
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = logging_propagate

    return logger
