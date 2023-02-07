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

def plot_filter_response(b, a, fs):
    w, h = freqz(b, a)
    plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
    plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
    plt.axvline(cutoff, color='k')
    plt.xlim(0, 0.5*fs)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain")

st.title("Butterworth Lowpass Filter Coefficients Calculator")

order = st.sidebar.slider("Filter Order", 1, 10, 5)
fs = st.sidebar.number_input("Sampling Frequency (Hz)", value=1000, min_value=1, max_value=10000, step=1)
cutoff = st.sidebar.number_input("Cutoff Frequency (Hz)", value=100, min_value=1, max_value=10000, step=1)

b, a = butter_lowpass(cutoff, fs, order)

plot_filter_response(b, a, fs)
st.pyplot()

st.write("Filter Order: ", order)
st.write("Sampling Frequency: ", fs, "Hz")
st.write("Cutoff Frequency: ", cutoff, "Hz")
st.write("Numerator (b) Coefficients: ", b)
st.write("Denominator (a) Coefficients: ", a)


