import logging

import pytest

from toolsy.logger import init_root_logger


class TestLogger:
    def test_logger(self):
        init_root_logger(__name__)
        logger = logging.getLogger(__name__)
        logger.info("Logger Test...")


if __name__ == '__main__':
    pytest.main([__file__])
