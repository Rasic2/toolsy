import pytest

from toolsy.logger import init_colored_logger


class TestLogger:
    def test_logger(self):
        logger = init_colored_logger(__name__)
        logger.info("Logger Test...")


if __name__ == '__main__':
    pytest.main([__file__])
