import numpy as np
import pandas as pd


def print_utils():
    return "Utils imported"


def pandas_utils():
    return pd.Series([1, 3, 5, np.nan, 6, 8])


def numpy_utils():
    return np.arange(15).reshape(3, 5)
