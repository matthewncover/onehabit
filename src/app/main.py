import streamlit as st

from .home import HomePage
from .welcome import WelcomePage
from .accounts.login import LoginPage
from .accounts.create import CreateAccountPage

from .editor import EditorPage
from .tracker import TrackerPage
from .analysis import AnalysisPage

from enum import Enum

class Pages(Enum):
    HomePage = HomePage
    WelcomePage = WelcomePage
    LoginPage = LoginPage
    CreateAccountPage = CreateAccountPage

    EditorPage = EditorPage
    TrackerPage = TrackerPage
    AnalysisPage = AnalysisPage

class GoalTrackingApp:

    def __init__(self):

        for page in Pages:
            setattr(self, page.name, page.value)

        st.session_state.setdefault("current_page", "HomePage")
        getattr(self, st.session_state.current_page)()