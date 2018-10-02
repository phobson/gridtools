from pkg_resources import resource_filename
from contextlib import contextmanager
from functools import wraps
import filecmp

try:
    import pytest
except ImportError:
    pytest = None

import numpy.testing as nptest
import pandas.util.testing as pdtest

import geopandas


def assert_textfiles_equal(baselinefile, outputfile):
    assert filecmp.cmp(baselinefile, outputfile)


def assert_gis_files_equal(baselinefile, outputfile, atol=0.001):
    expected = geopandas.read_file(baselinefile)
    result = geopandas.read_file(outputfile)
    pdtest.assert_frame_equal(
        result.drop('geometry', axis=1).sort_index(axis='columns'),
        expected.drop('geometry', axis=1).sort_index(axis='columns')
    )
    assert result.geom_almost_equals(expected).all()
