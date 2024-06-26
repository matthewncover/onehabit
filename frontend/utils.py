from typing import List
import time
import streamlit as st

from frontend import Tab
from onehabit.coach.openai.messages import Message

class StUtils:

    @staticmethod
    def back_button(page:str):
        back = st.button("Back")
        if back:
            st.session_state.current_page = page
            st.rerun()

    @classmethod
    def logout_button(cls, key:str):
        logout = st.button("logout", key=key)
        if logout:
            cls.logout()

    def logout():
        st.session_state.current_page = "WelcomePage"
        st.session_state.clear()
        st.rerun()
    
    @staticmethod
    def empty_lines(n=1):
        st.markdown("<br>"*n, unsafe_allow_html=True)
    
    @staticmethod
    def not_implemented():
        st.write("Not Implemented")

    @staticmethod
    def typewriter(text: str, speed: int = 40):
        """https://discuss.streamlit.io/t/st-write-typewritter/43111/3
        """
        # tokens = text.split()
        # tokens = list(text)
        tokens = [item for sublist in [list(x) + ["<br>"] for x in text.split("<br>")] for item in sublist]
        container = st.empty()
        for index in range(len(tokens) + 1):
            # curr_full_text = " ".join(tokens[:index])
            curr_full_text = "".join(tokens[:index])
            container.markdown(curr_full_text, unsafe_allow_html=True)
            time.sleep(1 / speed)

    @staticmethod
    def display_tabs(tab_names:List[str], tab_classes:List[Tab]):
        for tab_col, tab_cls in zip(st.tabs(tab_names), tab_classes):
            with tab_col:
                tab_cls()

    @classmethod
    def coach_oneoff_response(cls, prompt):
        messages = [Message.to_openai_format(role="system", content=prompt)]
        response = st.session_state.coach._respond(messages)
        cls.display_coach_response(response)

    @classmethod
    def coach_dialogue_response(cls):
        response = st.session_state.coach.respond()
        cls.display_coach_response(response)

    @staticmethod
    def display_coach_response(response: str):
        st_msg = st.chat_message("coach")
        with st_msg:
            StUtils.typewriter(response, speed=100)

    @staticmethod
    def display_dialogue(dialogue):
        for chat_message in dialogue.full_text:
            role, chat_text = Message.from_openai_format(chat_message)
            st_msg = st.chat_message(role)
            if role == "coach":
                st_msg.markdown(chat_text, unsafe_allow_html=True)
            else:
                st_msg.write(chat_text)
