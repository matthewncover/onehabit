import streamlit as st

from onehabit.coach import Coach
from onehabit.data import OneHabitDatabase
from onehabit.data.schemas import User

class UserState:
    def __init__(self, user: User):
        self._init_user(user)
        self.ohdb = OneHabitDatabase()

    def _init_user(self, user: User):
        user.init_coach_settings()
        self.user = user

    def load(self):
        st.session_state.current_page = self.user.data.current_page

        if self.user.coach_personality:
            st.session_state.coach = Coach(self.user)