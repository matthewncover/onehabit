## home page after login

import streamlit as st

from . import Page
from .utils import Utils

class HomePage(Page):

    def __init__(self):
        super().__init__()
        
        if st.button("Login"):
            st.session_state.current_page = "LoginPage"
            st.experimental_rerun()

        if st.button("Create an account"):
            st.session_state.current_page = "CreateAccountPage"
            st.experimental_rerun()