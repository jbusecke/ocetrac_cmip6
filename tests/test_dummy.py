import pytest
from ocetrac_cmip6.dummy_module import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
