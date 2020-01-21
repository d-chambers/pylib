"""
Simple test suite for pylib cookie cutter template.
"""

import pytest
from cookiecutter.utils import rmtree


@pytest.fixture()
def baked_project(cookies):
    """
    Delete the temporary directory that is created when executing the tests
    """
    result = cookies.bake()
    try:
        yield result
    finally:
        rmtree(str(result.project))


class TestBasicCompletion:
    """ Tests for basic completion of template. """

    def test_bake_with_defaults(self, baked_project):
        assert baked_project.project.isdir()
        assert baked_project.exit_code == 0
        assert baked_project.exception is None
        found_toplevel_files = [f.basename for f in baked_project.project.listdir()]
        assert "setup.py" in found_toplevel_files
        assert "python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files
