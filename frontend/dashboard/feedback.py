import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class FeedbackTab(Tab):

    def __init__(self):
        st.write("Feedback to dev form")
        StUtils.empty_lines(5)