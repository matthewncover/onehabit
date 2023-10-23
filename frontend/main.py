import streamlit as st

from .accounts.login import LoginPage
from .accounts.create import CreateAccountPage

from . import Page

from .why import WhyTab
from .editor import EditorTab
from .tracker import TrackerTab
from .analysis import AnalysisTab

from enum import Enum

class Tabs(Enum):
    why_tab = WhyTab
    EditorTab = EditorTab
    TrackerTab = TrackerTab
    AnalysisTab = AnalysisTab

class MainPage(Page):

    def __init__(self):
        _, col, _ = st.columns((1, 3, 1))

        with col:
            st.subheader("One Habit")

            tab_names = [":grey[Why]", ":orange[Tracker]", ":blue[Editor]", ":violet[Analysis]"]
            tab_classes = [x.value for x in Tabs]

            for tab, cls in zip(st.tabs(tab_names), tab_classes):
                with tab:
                    cls()

class Pages(Enum):
    LoginPage = LoginPage
    CreateAccountPage = CreateAccountPage
    MainPage = MainPage

class OneHabitApp:

    def __init__(self):

        for page in Pages:
            setattr(self, page.name, page.value)

        st.session_state.setdefault("current_page", "LoginPage")
        getattr(self, st.session_state.current_page)()