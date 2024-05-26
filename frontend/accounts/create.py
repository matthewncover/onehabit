import time
import streamlit as st

from frontend import Tab
from onehabit.data.schemas.users import User, NewUserValidationError

class AccountCreationTab(Tab):

    def __init__(self):
        super().__init__()
        self.create_account_form()

    def create_account_form(self):
        with st.form(key="account_form"):
            username_input = st.text_input("username", value="yeeeeee")
            password_input = st.text_input("password", type="password", value="yeeeeee")
            password_again_input = st.text_input("re-enter password", type="password", value="yeeeeee")
            age_input = st.text_input("age", help="analytics purposes only. your info is never shared.", value=18)
            email_input = st.text_input("email (optional)", help="no spam. password resetting purposes only.")

            if st.form_submit_button("create"):
                if self._username_exists(username_input):
                    st.error("username already exists. tough")

                elif password_input != password_again_input:
                    st.error("passwords don't match")

                else:
                    user_data = {
                        "username": username_input,
                        "email": None if not email_input else email_input,
                        "password": password_input,
                        "age": age_input
                    }
                    try:
                        st.session_state.user = User(**user_data)
                        st.success("right on")
                        time.sleep(1)

                        st.session_state.current_page = "DisclaimerPage"
                        st.rerun()

                    except NewUserValidationError as e:
                        for msg in e.display_msgs:
                            st.error(msg)

    def _username_exists(self, username_input):
        users = self.ohdb.pull(User, User.username == username_input)[0]
        return True if users else False