import streamlit as st

from . import Tab
from .utils import Utils

class AnalysisTab(Tab):

    def __init__(self):
        super().__init__()
        st.write("Analysis")