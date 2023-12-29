import streamlit as st

from frontend import Page
from frontend.introduction.utils import IntroUtils

class PhilosophyPage(Page):
    
    def __init__(self):

        with IntroUtils.default_col():
            st.write("onehabit philosophy")
            ## hypotheses

            IntroUtils.back_save_continue(continue_to="CoachIntroductionPage")
            
            pass