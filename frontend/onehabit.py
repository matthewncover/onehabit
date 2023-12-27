from enum import Enum

import streamlit as st

from .welcome import WelcomePage
from .dashboard.dashboard import UserDashboardPage

class Pages(Enum):
    WelcomePage = WelcomePage
    UserDashboardPage = UserDashboardPage

class OneHabitApp:

    def __init__(self):

        for page in Pages:
            setattr(self, page.name, page.value)

        st.session_state.setdefault("current_page", "WelcomePage")
        getattr(self, st.session_state.current_page)()