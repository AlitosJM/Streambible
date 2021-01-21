# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd
import neattext.functions as nfx
import random


# Data Viz Pkgs
import altair as alt
import matplotlib

matplotlib.use("Agg")


def main():
    st.title("StreamBible")
    # stc.html(HTML_BANNER)
    menu = ["Home", "MultiVerse", "About"]

    # df = load_bible("data/KJV_Bible.csv")

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Single Verse Search")
    if choice == "MultiVerse":
        st.subheader("MultiVerse Retrieval")
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
