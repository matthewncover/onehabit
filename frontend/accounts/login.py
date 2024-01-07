from typing import List
import streamlit as st

from frontend import Tab
from frontend.accounts.load_state import UserState

from onehabit.data.encryption import EncryptionUtils
from onehabit.data.schemas.users import User

class AccountLoginTab(Tab):

    def __init__(self):
        super().__init__()
        self.login_form()
        
    def login_form(self):
        with st.form(key="login_form"):
            username_input = st.text_input("username", value="matthew")
            password_input = st.text_input("password", type="password", value="yeet-salad")

            if st.form_submit_button("login"):
                users: List[User] = self.ohdb.pull(User, User.username == username_input)
                if not users:
                    st.error("user not found. tough.")

                else:
                    user = users[0]

                    hashed_password = user.password_hash
                    if password_input is not None and hashed_password is not None:
                        password_validated = EncryptionUtils.check_password(hashed_password, password_input)

                        if hashed_password and password_validated:
                            st.session_state.user = user
                            user_state = UserState(user)
                            user_state.load()
                            
                            st.success("success")
                            st.rerun()

                        else:
                            st.error("incorrect password")



    