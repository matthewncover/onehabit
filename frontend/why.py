import streamlit as st

from . import Tab
from .utils import Utils

class WhyTab(Tab):

    def __init__(self):
        st.write("<Primary and secondary effects>, etc.")
        Utils.empty_lines(5)
        Utils.logout_button()