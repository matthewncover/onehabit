import streamlit as st
import bcrypt

from .. import Page
from ..utils import Utils

from onehabit import OneHabitDatabase

class CreateAccountPage(Page):

    def __init__(self):
        super().__init__()

        _, col, back_col = st.columns(3)
        with col:
            st.header("Create Account")
            self.create_account_form()

        with back_col:
            Utils.empty_lines(20)
            Utils.back_button("LoginPage")

    def create_account_form(self):
        with st.form(key="account_form"):
            username_input = st.text_input("Username")
            password_input = st.text_input("Password", type="password")
            password_again_input = st.text_input("Re-enter password", type="password")
            email_input = st.text_input("Email (super optional)")

            if st.form_submit_button("Yeet"):
                pass
                ## check if username already exists
                ## require username to be at least 5 characters, and not contain any special characters or whitespace
                ## require password to be at least 7 characters
                ## check that the two passwords entered match
                ## validate email with regex if not None

    def _check_username_exists(self):
        gtdb = OneHabitDatabase()

    def hash_password(password):
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )