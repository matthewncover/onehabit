import streamlit as st
import bcrypt

from .. import Page
from ..utils import Utils

class CreateAccountPage(Page):

    def __init__(self):
        super().__init__()

        _, col, back_col = st.columns(3)
        with col:
            st.header("Create Account")
            self.create_account_form()

        with back_col:
            Utils.back_button("HomePage")

    def create_account_form(self):
        with st.form(key="account_form"):
            username_input = st.text_input("Username")
            password_input = st.text_input("Password", type="password")
            password_again_input = st.text_input("Re-enter password", type="password")
            email_input = st.text_input("Email (super optional)")

            if st.form_submit_button("Yeet"):
                pass
                ## check if username already exists
                ## require username to be at least 5 characters
                ## require username not contain any special characters or whitespace
                ## verify they've entered a password
                ## require password to be at least 7 characters
                ## validate email with regex if not None

    def hash_password(password):
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )