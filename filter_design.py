"""Utility functions for Butterworth low-pass filter design and visualization."""

from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz


def butter_lowpass(cutoff: float, fs: float, order: int = 5) -> Tuple[np.ndarray, np.ndarray]:
    """Design a digital Butterworth low-pass filter.

    Parameters
    ----------
    cutoff: float
        Cutoff frequency in Hz.
    fs: float
        Sampling frequency in Hz.
    order: int, default=5
        Order of the filter.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Numerator (``b``) and denominator (``a``) filter coefficients.
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    return b, a


def plot_filter_response(
    b: np.ndarray, a: np.ndarray, fs: float, width: int, height: int
) -> plt.Figure:
    """Plot the magnitude and phase response of a digital filter.

    Parameters
    ----------
    b, a: np.ndarray
        Filter coefficients.
    fs: float
        Sampling frequency in Hz.
    width, height: int
        Size of the resulting chart in inches.

    Returns
    -------
    matplotlib.figure.Figure
        Figure containing the frequency response plot.
    """
    w, h = freqz(b, a)
    fig, ax1 = plt.subplots(figsize=(width, height))
    ax1.plot(0.5 * fs * w / np.pi, np.abs(h), "b")
    ax1.set_xlim(0, 0.5 * fs)
    ax1.set_ylim(0, 1.1)
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Gain", color="b")
    ax1.grid(True)

    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.plot(0.5 * fs * w / np.pi, angles, "g")
    ax2.set_ylabel("Phase (radians)", color="g")
    ax2.grid(False)

    fig.suptitle("Butterworth Lowpass Filter Response")
    return fig
