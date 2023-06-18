import streamlit as st
from database import GoalsDataBase

import datetime as dt

class Base:
    pass

class GoalTrackingApp(Base):

    #region init
    def __init__(self):
        super().__init__()

        self.secrets = st.secrets["secrets"]

    def run(self):
        self.page_login()

    #endregion
    #region database
    
    @st.cache_resource
    def _init_db(self):
        self.db = GoalsDataBase()
        self.db.connect(self.secrets)

    @st.cache_data
    def push_data(self, table_name:str, data:dict):
        self.db.push(table_name, data)

    @st.cache_data
    def pull_data(self, table_name:str, query_condition:str=None):
        self.db.pull(table_name, query_condition)
    
    #endregion
    #region login

    def page_login(self):

        logged_in = st.session_state.get("logged_in", False)

        if not logged_in:
            passphrase = st.text_input("passphrase:")

            if passphrase:
                if passphrase == self.secrets["PASSPHRASE"]:
                    st.session_state.logged_in = True
                    st.success("good to see you")
                    st.experimental_rerun()
                else:
                    st.error("nope")
        
        else:
            self.sidebar_pages()

    def sidebar_pages(self):
        page_dict = {
            "goals": self.page_okrs,
            "survey": self.page_survey,
        }

        page_names = list(page_dict.keys())
        page = st.sidebar.radio("Select a page", page_names, label_visibility='collapsed')

        page_dict[page]()

    def page_okrs(self):
        st.write("goals")

    def page_survey(self):
        st.write("hey")



    #endregion
    #region

    #endregion

if __name__ == "__main__":
    app = GoalTrackingApp()
    app.run()