import streamlit as st

from frontend import Page
from frontend.utils import StUtils
from frontend.texts import COACH_INTRO_TEXT
from frontend.introduction.utils import IntroUtils

from frontend.tmp_prompts import COACH_PERSONALITY_INTRO_PROMPT

from onehabit.coach.openai.models import Coach
from onehabit.data.schemas import Personality

class CoachIntroductionPage(Page):
    
    def __init__(self):
        st.session_state.setdefault("personalities", self.ohdb.pull(Personality))
        st.session_state.setdefault("coach_personality_obj", None)
        st.session_state.coach: Coach

        with IntroUtils.default_col():
            st.markdown(COACH_INTRO_TEXT)

            with st.columns(2)[0]:
                personalities = ["select one"] + [x.name for x in st.session_state.personalities]
                chosen_personality_name = st.selectbox(label="style", options=personalities)

            if chosen_personality_name != "select one":
                personality_obj: Personality = self.get_personality_obj(chosen_personality_name)
                st.session_state.coach_personality_obj = personality_obj
                StUtils.coach_oneoff_response(COACH_PERSONALITY_INTRO_PROMPT + personality_obj.description)
                self.update_coach_personality_preference(personality_obj)

            if chosen_personality_name != "select one":
                StUtils.empty_lines(1)
                IntroUtils.back_save_continue(
                    back_to="PhilosophyPage",
                    continue_to="HabitIntroductionPage"
                    )
                
    def get_personality_obj(self, chosen_personality_name:str):
        return [
            x for x in st.session_state.personalities 
            if x.name == chosen_personality_name
            ][0]
    
    def update_coach_personality_preference(self, personality_obj: Personality):
        setattr(st.session_state.user.data, 'coach_personality_id', personality_obj.id)
        self.ohdb.update(st.session_state.user)