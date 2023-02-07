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
    plt.figure(figsize=(width, height))
    plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
    plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
    plt.axvline(cutoff, color='k')
    plt.xlim(0, 0.5*fs)
    plt.grid(True)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain")

st.title("Butterworth Lowpass Filter Coefficients Calculator")

order = st.sidebar.slider("Filter Order", 1, 10, 5)
fs = st.sidebar.number_input("Sampling Frequency (Hz)", value=1000, min_value=1, max_value=10000, step=1)
cutoff = st.sidebar.number_input("Cutoff Frequency (Hz)", value=100, min_value=1, max_value=10000, step=1)

b, a = butter_lowpass(cutoff, fs, order)

width = st.sidebar.number_input("Chart Width", value=6, min_value=1, max_value=20, step=1)
height = st.sidebar.number_input("Chart Height", value=4, min_value=1, max_value=20, step=1)

plot_filter_response(b, a, fs, width, height)
st.pyplot()

st.write("Numerator (b) Coefficients: ", b)
st.write("Denominator (a) Coefficients: ", a)
