import streamlit as st

from frontend import Page
from frontend.texts import HABIT_INTRO_TEXT
from frontend.introduction.utils import IntroUtils
from frontend.utils import StUtils

class HabitIntroductionPage(Page):
    
    def __init__(self):
        with IntroUtils.default_col():
            st.markdown(HABIT_INTRO_TEXT, unsafe_allow_html=True)
            
            StUtils.empty_lines(1)
            IntroUtils.back_save_continue(
                back_to="CoachIntroductionPage",
                continue_to="HabitIdentificationPage"
            )
