import streamlit as st

from frontend.texts import WELCOME_TEXT
from frontend.utils import StUtils
from frontend.accounts.login import AccountLoginTab
from frontend.accounts.create import AccountCreationTab

class WelcomePage:
    def __init__(self):
        preview_col, sign_in_col = st.columns((3, 2))

        with preview_col:
            _, content_col, _ = st.columns((5, 10, 1))

            with content_col:
                # StUtils.typewriter(WELCOME_TEXT, speed=300)
                pass

        with sign_in_col:
            _, account_col, _ = st.columns((1, 20, 5))
            tab_names = [":white[login]", ":white[create account]"]
            tab_classes = [AccountLoginTab, AccountCreationTab]

            with account_col:
                st.markdown("<br>"*2, unsafe_allow_html=True)
                st.markdown("##### OneHabit", unsafe_allow_html=True)
                StUtils.display_tabs(tab_names, tab_classes)