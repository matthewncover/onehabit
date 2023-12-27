from contextlib import ContextDecorator
import streamlit as st

from frontend.utils import StUtils
from frontend.accounts.login import AccountLoginTab
from frontend.accounts.create import AccountCreationTab

class WelcomePage:
    def __init__(self):

        preview_col, sign_in_col = st.columns((3, 2))

        with preview_col:
            _, content_col, _ = st.columns((5, 10, 1))

            welcome_msg = """<br><br><br><br>
            set expectations low, insultingly low.<br><br>
            see your habit as a much more than just a task.<br><br>
            track progress, build momentum.<br><br>
            get rewarded for honesty when you miss the mark.<br><br>
            build awareness of what's holding you back.<br><br>
            become whom you could be, starting with one habit.
            """
            with content_col:
                StUtils.typewriter(welcome_msg, speed=300)

        with sign_in_col:
            _, account_col, _ = st.columns((1, 20, 5))
            tab_names = [":white[login]", ":white[create account]"]
            tab_classes = [AccountLoginTab, AccountCreationTab]

            with account_col:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("##### OneHabit", unsafe_allow_html=True)
                StUtils.display_tabs(tab_names, tab_classes)