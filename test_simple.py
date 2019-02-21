# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name
"""Test simple Python script."""
from langsamt import add_two


def test_plus2():
    """Test adding 2. """
    assert add_two(5) == 7
