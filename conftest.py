import warnings
import pytest

def pytest_configure():
    warnings.filterwarnings(
        "ignore",
        message=".*asyncio_default_fixture_loop_scope.*",
        category=pytest.PytestDeprecationWarning,
    )
