import streamlit as st

from frontend.pages import Pages

class OneHabitApp:

    def __init__(self):

        for page in Pages:
            setattr(self, page.name, page.value)

        st.session_state.setdefault("current_page", "WelcomePage")
        getattr(self, st.session_state.current_page)()