import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class CoachTab(Tab):

    def __init__(self):
        st.write("discuss with coach")
        StUtils.empty_lines(5)