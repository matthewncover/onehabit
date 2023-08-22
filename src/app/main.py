import streamlit as st

from .welcome import WelcomePage
from .login import LoginPage
from .editor import EditorPage
from .tracker import TrackerPage
from .analysis import AnalysisPage

from enum import Enum

class Pages(Enum):
    WelcomePage = WelcomePage
    LoginPage = LoginPage
    EditorPage = EditorPage
    TrackerPage = TrackerPage
    AnalysisPage = AnalysisPage

class GoalTrackingApp:

    def __init__(self):

        for page in Pages:
            setattr(self, page.name, page.value)

        st.session_state.setdefault("current_page", "WelcomePage")
        getattr(self, st.session_state.current_page)()