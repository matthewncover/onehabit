import streamlit as st

from frontend import Page
from frontend.utils import StUtils
from frontend.texts import HABIT_IDENTIFICATION_TEXT
from frontend.introduction.utils import IntroUtils

from onehabit.data.schemas import Dialogue
from onehabit.data.db_utils import DatabaseUtils

class HabitIdentificationPage(Page):

    NAME = "introduction.habit_identification"
    
    def __init__(self):
        self.dialogue: Dialogue = st.session_state.coach.open_dialogue(self.NAME)

        with IntroUtils.default_col():
            st.markdown(HABIT_IDENTIFICATION_TEXT, unsafe_allow_html=True)

            if self.dialogue is None:
                if st.button("Start discussion"):
                    DatabaseUtils.make_new_dialogue(
                        st.session_state.user.id, self.NAME
                    )
                    self.dialogue = st.session_state.coach.open_dialogue(self.NAME)

            else:

                if not self.dialogue.full_text:
                    self.coach_response()
                else:
                    StUtils.display_dialogue(self.dialogue)
                    st.session_state.discussion_turn = st.session_state.coach.next_role()

                if st.session_state.discussion_turn == "coach":
                    self.coach_response()
                else:
                    self.user_response()

                StUtils.empty_lines(2)
            IntroUtils.back_save_continue(
                back_to="HabitIntroductionPage",
                continue_to="HabitDefinitionPage")
            
    def coach_response(self):
        StUtils.coach_dialogue_response()
        st.session_state.discussion_turn = "user"
        st.rerun()

    def user_response(self):
        with st.form("user response"):
            msg_no = st.session_state.coach.n_messages()
            user_response = st.text_area(
                label=st.session_state.user.username, max_chars=4000, 
                key=f"habit_ident_dialogue-msg#{msg_no}")
            
            if st.form_submit_button("send"):    
                st.session_state.coach.update_dialogue(role="user", response=user_response)
                st.session_state.discussion_turn = "coach"
                st.rerun()