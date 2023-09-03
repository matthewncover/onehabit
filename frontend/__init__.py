import streamlit as st

from ..data.database import OneHabitDatabase

class Page:
    
    def __init__(self):
        st.header("One Habit")
        st.divider()

        self.gtdb = OneHabitDatabase()