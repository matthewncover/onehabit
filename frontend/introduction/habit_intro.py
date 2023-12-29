import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class HabitIntroductionPage(Page):
    
    def __init__(self):
        continue_to = None

        with IntroUtils.default_col():
            st.write("habit introduction")
            
            st.markdown("||text||<br><br>", unsafe_allow_html=True)
            
            radio_options = {
                "not quite sure, let me think it through with Coach": "CoachHabitDiscussionPage",
                "yeah, i have my one habit in mind": "HabitDefinitionPage"
            }
            
            habit_radio = st.radio(label="ready?", options=radio_options)

            continue_to = radio_options.get(habit_radio, None)

            IntroUtils.back_save_continue(
                back_to="CoachIntroductionPage",
                continue_to=continue_to
            )
