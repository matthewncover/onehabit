import streamlit as st

from frontend import Page
from frontend.texts import PHILOSOPHY_TEXT
from frontend.introduction.utils import IntroUtils

class PhilosophyPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.markdown(PHILOSOPHY_TEXT, unsafe_allow_html=True)

            IntroUtils.back_save_continue(continue_to="CoachIntroductionPage")