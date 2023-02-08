import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

st.set_option('deprecation.showPyplotGlobalUse', False)

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def plot_filter_response(b, a, fs, width, height):
    w, h = freqz(b, a)
    fig, ax1 = plt.subplots(figsize=(width, height))
    plt.subplot(1, 1, 1)
    ax1.plot(0.5*fs*w/np.pi, abs(h), 'b')
    ax1.set_xlim(0, 0.5*fs)
    ax1.set_ylim(0, 1.1)
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Gain', color='b')
    ax1.grid(True)
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.plot(0.5*fs*w/np.pi, angles, 'g')
    ax2.set_ylabel('Phase (radians)', color='g')
    ax2.grid(False)
    plt.title("Butterworth Lowpass Filter Response")

st.set_page_config(page_title="Butterworth Lowpass Filter Coefficients Calculator")

st.title("Butterworth Lowpass Filter Coefficients Calculator")

order = st.sidebar.slider("Filter Order", 1, 10, 2)
fs = st.sidebar.number_input("Sampling Frequency (Hz)", value=100, min_value=1, max_value=1000, step=1)
cutoff = st.sidebar.number_input("Cutoff Frequency (Hz)", value=20, min_value=1, max_value=1000, step=1)

b, a = butter_lowpass(cutoff, fs, order)

width = st.sidebar.number_input("Chart Width", value=12, min_value=1, max_value=20, step=1)
height = st.sidebar.number_input("Chart Height", value=8, min_value=1, max_value=20, step=1)

plot_filter_response(b, a, fs, width, height)
st.pyplot()

st.write("Numerator (b) Coefficients: ", b)
st.write("Denominator (a) Coefficients: ", a)
