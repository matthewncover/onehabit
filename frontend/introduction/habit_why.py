import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class HabitWhyPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.write("habit why page")

            IntroUtils.back_save_continue(
                back_to="HabitDefinitionPage",
                continue_to="HabitSummaryPage")
