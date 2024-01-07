import streamlit as st
from onehabit.data import OneHabitDatabase
from onehabit.coach.openai.models import Coach

class StBase:
    if "user" in st.session_state:
        st.session_state.setdefault("coach", Coach(user=st.session_state.user))

class Page (StBase):
    ohdb = OneHabitDatabase()

    @classmethod
    def update_user_current_page(cls, page_name:str):
        st.session_state.user.data.current_page = page_name
        st.session_state.current_page = page_name
        cls.ohdb.update(st.session_state.user)

class Tab (StBase):
    ohdb = OneHabitDatabase()