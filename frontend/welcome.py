import streamlit as st

from . import Page
from .utils import Utils

class WelcomePage(Page):

    def __init__(self):
        super().__init__()
        st.subheader("Welcome")

        _, col, _ = st.columns((2, 4, 2))

        with col:
            with st.expander("Why am I doing this again?"):
                st.write("<Primary and secondary effects>, etc.")

            Utils.logout_button()