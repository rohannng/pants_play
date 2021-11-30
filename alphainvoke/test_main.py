from alphainvoke import main
import pandas as pd
import numpy as np


def test_pandas_signal():
    pd.testing.assert_series_equal(main.pandas_signal(), pd.Series([1, 3, 5, np.nan, 6, 8]))


def test_numpy_signal():
    np.testing.assert_array_equal(main.numpy_signal(), np.arange(15).reshape(3, 5))
