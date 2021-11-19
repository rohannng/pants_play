import alphacommon.utils
import pandas as pd
import numpy as np


def test_print_utils():
    assert  alphacommon.utils.print_utils() == "Utils imported"


def test_pandas_utils():
    assert alphacommon.utils.pandas_utils() == pd.Series([1, 3, 5, np.nan, 6, 8])


def test_numpy_utils():
    assert alphacommon.utils.numpy_utils() == np.arange(15).reshape(3, 5)

