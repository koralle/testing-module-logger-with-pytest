from contextlib import contextmanager
from logging import Logger
from typing import Generator, List, Tuple

import pytest
from _pytest.logging import LogCaptureHandler


class LogLocalCaptureFixture:
    def __init__(self: "LogLocalCaptureFixture"):
        self.handler = LogCaptureHandler()

    @contextmanager
    def __call__(
        self: "LogLocalCaptureFixture", level: int, logger: Logger
    ) -> Generator[None, None, None]:

        orig_level = logger.level
        logger.setLevel(level)

        logger.addHandler(self.handler)
        try:
            yield
        finally:
            logger.setLevel(orig_level)
            logger.removeHandler(self.handler)

    @property
    def record_tuples(self: "LogLocalCaptureFixture") -> List[Tuple[str, int, str]]:
        return [(r.name, r.levelno, r.getMessage()) for r in self.handler.records]


@pytest.fixture
def local_caplog() -> Generator[LogLocalCaptureFixture, None, None]:
    yield LogLocalCaptureFixture()
