import streamlit as st

from frontend import Page
from frontend.utils import StUtils

class IntroUtils:

    @staticmethod
    def default_col():
        _, col, _ = st.columns((1, 3, 1))
        return col

    @staticmethod
    def back_save_continue(back_to:str=None, continue_to:str=None):
        back_col, save_exit_col, continue_col = st.columns(3)

        back_disabled = not bool(back_to)
        continue_disabled = not bool(continue_to)

        if back_col.button("back", disabled=back_disabled):
            st.session_state.current_page = back_to
            Page.update_user_current_page(back_to)
            st.rerun()

        if save_exit_col.button("save + logout"):
            StUtils.logout()
        
        if continue_col.button("continue", disabled=continue_disabled):
            st.session_state.current_page = continue_to
            Page.update_user_current_page(continue_to)
            st.rerun()