import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class EditorTab(Tab):

    def __init__(self):
        super().__init__()
        st.write("Editor")