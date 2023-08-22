import streamlit as st

from . import Page
from .utils import Utils

class WelcomePage(Page):

    def __init__(self):
        Utils.not_implemented()

        login_page = st.button("Login")
        if login_page:
            st.session_state.current_page = "LoginPage"
            st.experimental_rerun()