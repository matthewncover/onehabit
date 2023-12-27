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
            username_input = st.text_input("username")
            password_input = st.text_input("password", type="password")
            password_again_input = st.text_input("re-enter password", type="password")
            email_input = st.text_input("email (optional)")

            if st.form_submit_button("create"):
                if self._username_exists(username_input):
                    st.error("username already exists")

                elif password_input != password_again_input:
                    st.error("passwords don't match")

                else:
                    user_data = {
                        "username": username_input,
                        "email": None if not email_input else email_input,
                        "password": password_input
                    }
                    try:
                        user = User(**user_data)
                        self.ohdb.add(user)
                        st.success("right on")
                        time.sleep(1)

                        ## TODO
                        ## go to introduction

                    except NewUserValidationError as e:
                        for msg in e.display_msgs:
                            st.error(msg)

    def _username_exists(self, username_input):
        users = self.ohdb.pull(User, User.username == username_input)
        return True if users else False