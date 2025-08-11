"""Streamlit application for designing Butterworth low-pass filters."""

import streamlit as st

from filter_design import butter_lowpass, plot_filter_response


def main() -> None:
    """Render the Streamlit user interface."""
    st.set_page_config(page_title="Butterworth Lowpass Filter Coefficients Calculator")
    st.title("Butterworth Lowpass Filter Coefficients Calculator")

    order = st.sidebar.slider("Filter Order", 1, 10, 2)
    fs = st.sidebar.number_input(
        "Sampling Frequency (Hz)", value=100, min_value=1, max_value=1000, step=1
    )
    cutoff = st.sidebar.number_input(
        "Cutoff Frequency (Hz)", value=20, min_value=1, max_value=1000, step=1
    )
    b, a = butter_lowpass(cutoff, fs, order)

    width = st.sidebar.number_input("Chart Width", value=12, min_value=1, max_value=20, step=1)
    height = st.sidebar.number_input("Chart Height", value=8, min_value=1, max_value=20, step=1)

    fig = plot_filter_response(b, a, fs, width, height)
    st.pyplot(fig)
    st.write("Numerator (b) Coefficients: ", b)
    st.write("Denominator (a) Coefficients: ", a)


if __name__ == "__main__":
    main()
