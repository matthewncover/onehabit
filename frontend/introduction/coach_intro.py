import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class CoachIntroductionPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.write("introduction to coach")
            ## 
            ## set coach's style
            
            IntroUtils.back_save_continue(
                back_to="PhilosophyPage",
                continue_to="HabitIntroductionPage"
                )