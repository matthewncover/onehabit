import streamlit as st
from onehabit.data import OneHabitDatabase

class Page:
    ohdb = OneHabitDatabase()

    @classmethod
    def update_user_current_page(cls, page_name:str):
        st.session_state.user.data.current_page = page_name
        st.session_state.current_page = page_name
        cls.ohdb.update(st.session_state.user)

class Tab:
    ohdb = OneHabitDatabase()