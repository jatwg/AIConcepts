import streamlit as st
import os

def display_welcome():
    st.sidebar.write(f"Welcome: {os.getlogin()}")
