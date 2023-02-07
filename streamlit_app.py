import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

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
fs = st.sidebar.slider("Sampling Frequency (Hz)", 1, 10000, 1000)
cutoff = st.sidebar.slider("Cutoff Frequency (Hz)", 1, 10000, 100)

b, a = butter_lowpass(cutoff, fs, order)

st.write("Filter Order: ", order)
st.write("Sampling Frequency: ", fs, "Hz")
st.write("Cutoff Frequency: ", cutoff, "Hz")
st.write("Numerator (b) Coefficients: ", b)
st.write("Denominator (a) Coefficients: ", a)

plot_filter_response(b, a, fs)
st.pyplot()
