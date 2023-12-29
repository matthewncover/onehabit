import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class HabitDefinitionPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.write("habit definition")
            
            IntroUtils.back_save_continue(
                back_to="HabitIntroductionPage",
                continue_to="HabitWhyPage")
