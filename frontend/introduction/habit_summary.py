import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class HabitSummaryPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.write("habit summary page")
            st.write("you're going to be stuck with this, you won't be able to edit your habit or add a new one until you prove yourself. look good?")
            
            IntroUtils.back_save_continue(
                back_to="HabitWhyPage",
                continue_to="UserDashboardPage")
