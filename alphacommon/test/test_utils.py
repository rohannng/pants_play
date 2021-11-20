from alphacommon.alphacommon import utils
import pandas as pd
import numpy as np


def test_print_utils():
    assert utils.print_utils() == "Utils imported"


def test_pandas_utils():
    print(utils.pandas_utils())
    pd.testing.assert_series_equal(utils.pandas_utils(), pd.Series([1, 3, 5, np.nan, 6, 8]))


def test_numpy_utils():
    print ( utils.numpy_utils())
    np.testing.assert_array_equal(utils.numpy_utils(), np.arange(15).reshape(3, 5))
