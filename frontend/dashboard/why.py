import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class WhyTab(Tab):

    def __init__(self):
        st.write("<Primary and secondary effects>, etc.")
        StUtils.empty_lines(5)