import sys

from substratools import exceptions, Metrics
from substratools.utils import import_module, load_interface_from_module

import pytest


def test_invalid_interface():
    code = """
def score():
    pass
"""
    import_module('score', code)
    with pytest.raises(exceptions.InvalidInterface):
        load_interface_from_module('score', interface_class=Metrics)


@pytest.fixture
def syspaths():
    copy = sys.path[:]
    yield sys.path
    sys.path = copy


def test_empty_module(tmpdir, syspaths):
    with tmpdir.as_cwd():
        # python allows to import an empty directoy
        # check that the error message would be helpful for debugging purposes
        tmpdir.mkdir("foomod")
        syspaths.append(str(tmpdir))

        with pytest.raises(exceptions.EmptyInterface):
            load_interface_from_module('foomod', interface_class=Metrics)
