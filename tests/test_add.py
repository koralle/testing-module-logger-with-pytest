from logging import DEBUG

from _pytest.logging import LogCaptureFixture

from src.lib_with_module_logger import add as module_add
from src.lib_with_root_logger import add as root_add
from src.loggers import create_module_logger
from tests.conftest import LogLocalCaptureFixture


class TestLogging:
    def test_ルートロガーではcaplogをそのまま使えばログををキャプチャできる(
        self: "TestLogging", caplog: LogCaptureFixture
    ):
        # DEBUG以上のレベルのログをキャプチャする
        caplog.set_level(DEBUG)

        # 関数の実行(と同時にDEBUGログを吐く)
        expect: int = 9
        _ = root_add(a=4, b=5)
        assert [("root", DEBUG, f"result: {expect}")] == caplog.record_tuples

    def test_モジュールロガーでもルートロガーまでログが伝播するならcaplogでログをキャプチャすることができる(
        self: "TestLogging", caplog: LogCaptureFixture
    ) -> None:
        logger_name = "TestLogger"
        logger = create_module_logger(logger_name=logger_name, logging_propagate=True)

        # DEBUG以上のレベルのログをキャプチャする
        caplog.set_level(DEBUG)

        expect: int = 9
        # 関数の実行(と同時にDEBUGログを吐く)
        _ = module_add(a=4, b=5, logger=logger)
        assert [(logger_name, DEBUG, f"result: {expect}")] == caplog.record_tuples

    def test_モジュールロガーはルートロガーまでログが伝播しないとcaplogでログをキャプチャすることができない(
        self: "TestLogging", caplog: LogCaptureFixture
    ) -> None:
        logger_name = "TestLogger"
        logger = create_module_logger(logger_name=logger_name, logging_propagate=False)

        # DEBUG以上のレベルのログをキャプチャする
        caplog.set_level(DEBUG)

        expect: int = 9
        # 関数の実行(と同時にDEBUGログを吐く)
        _ = module_add(a=4, b=5, logger=logger)
        assert (logger_name, DEBUG, f"result: {expect}") not in caplog.record_tuples

    def test_モジュールロガーではlocal_caplogを使うことでlogをキャプチャできる(
        self: "TestLogging", local_caplog: LogLocalCaptureFixture
    ):
        logger_name = "TestLogger"
        logger = create_module_logger(logger_name=logger_name, logging_propagate=False)

        with local_caplog(DEBUG, logger=logger):
            expect: int = 9
            # 関数の実行（と同時にDEBUGログを吐く）
            _ = module_add(a=4, b=5, logger=logger)
            assert [
                (logger_name, DEBUG, f"result: {expect}")
            ] == local_caplog.record_tuples
