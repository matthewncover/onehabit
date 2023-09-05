import streamlit as st

from . import Tab
from .utils import Utils

class EditorTab(Tab):

    def __init__(self):
        super().__init__()
        st.write("Editor")