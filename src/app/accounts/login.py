import streamlit as st
import bcrypt

from .. import Page
from ..utils import Utils

class LoginPage(Page):

    def __init__(self):
        super().__init__()
        
        _, col, _ = st.columns(3)
        with col:
            st.header("Login")
            self.login_form()

        if col.button("Create account"):
            st.session_state.current_page = "CreateAccountPage"
            st.experimental_rerun()

    def login_form(self):
        with st.form(key="login_form"):
            
            username_input = st.text_input("Username")
            password_input = st.text_input("Password", type="password")

            if st.form_submit_button("Submit"):
                hashed_password = self.gtdb.get_password(username=username_input)
                if password_input is not None and hashed_password is not None:
                    password_validated = self._check_password(hashed_password, password_input)

                    if hashed_password and password_validated:
                        st.session_state.current_page = "WelcomePage"
                        st.success("Success")
                        st.experimental_rerun()

                    else:
                        st.error("Incorrect password")

                else:
                    st.error(f"User 'matthew' not found.")

    def _check_password(self, hashed_password, password_input):
        return bcrypt.checkpw(
            password=password_input.encode('utf-8'),
            hashed_password=hashed_password
        )

    