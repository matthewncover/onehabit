from typing import List
import time

import streamlit as st

from frontend import Tab

class StUtils:

    @staticmethod
    def back_button(page:str):
        back = st.button("Back")
        if back:
            st.session_state.current_page = page
            st.rerun()

    @staticmethod
    def logout_button(key:str):
        logout = st.button("logout", key=key)
        if logout:
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
    def display_tabs(tab_names:List[str], tab_classes:List[Tab]):
        for tab_col, tab_cls in zip(st.tabs(tab_names), tab_classes):
            with tab_col:
                tab_cls()

    @staticmethod
    def typewriter(text: str, speed: int = 10):
        """ credit: https://discuss.streamlit.io/t/st-write-typewritter/43111/3
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

    ## BUG
    ## does not work
    @staticmethod
    def aligned_text(text:str, how="center"):
        st.markdown(f"<text style='text-align: {how}; color: white;'>{text}</text>", unsafe_allow_html=True)