import streamlit as st
from database import GoalsDataBase

class Base:
    pass

class GoalTrackingApp(Base):

    #region init
    def __init__(self):
        super().__init__()

        self.secrets = st.secrets["secrets"]

    def _init_db(self):
        self.db = GoalsDataBase()
        self.db.connect(self.secrets)

    #endregion
    #region login

    def login_page(self):

        logged_in = st.session_state.get("logged_in", False)

        if not logged_in:
            passphrase = st.text_input("passphrase:")

            if passphrase == self.secrets["PASSPHRASE"]:
                st.session_state.logged_in = True
                st.success()
                # st.experimental_rerun
            else:
                st.error("nope")

    #endregion
    #region
    
    #endregion