"""Simple maths functions that aren't implemented in python math
"""

def clip(x: float, xmin: float, xmax: float):
    """Clip a number between a minimum and maximum.

    Parameters
    ----------
    x : float
        Value to clip
    xmin : float
        Minimum for value.
    xmax : float
        Maximum for value.

    Returns
    -------
    float
        Clipped value.
    """
    return max(min(x, xmax),xmin)