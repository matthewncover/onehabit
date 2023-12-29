import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class CoachHabitDiscussionPage(Page):
    
    def __init__(self):
        continue_to = None

        with IntroUtils.default_col():
            st.write("habit discussion page")
            ## get information from the user to prep the discussion
            ##      figure out values first?
            IntroUtils.back_save_continue(
                back_to="HabitIntroductionPage",
                continue_to="HabitDefinitionPage")
