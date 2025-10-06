"""
Linear Regression implementation from scratch using NumPy.
"""

from .linear_regression import LinearRegression
from .utils import (
    load_data,
    train_test_split,
    normalize,
    calculate_mse,
    calculate_r2,
    plot_predictions,
    plot_residuals
)

__version__ = "0.1.0"
__all__ = [
    "LinearRegression",
    "load_data",
    "train_test_split",
    "normalize",
    "calculate_mse",
    "calculate_r2",
    "plot_predictions",
    "plot_residuals"
]