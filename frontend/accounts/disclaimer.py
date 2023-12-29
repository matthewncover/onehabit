import time
import streamlit as st

from frontend import Page
from frontend.texts import DISCLAIMER_TEXT

class DisclaimerPage(Page):
    
    def __init__(self):
        _, col, _ = st.columns((1, 3, 1))

        with col:
            st.markdown(DISCLAIMER_TEXT, unsafe_allow_html=True)
            
            accept_col, reject_col = st.columns(2)

            if accept_col.button("sounds good"):
                self.ohdb.add(st.session_state.user)
                st.success("sick, account made!")
                time.sleep(2)
                
                self.update_user_current_page("PhilosophyPage")
                st.rerun()

            if reject_col.button("hard pass, thanks"):
                st.session_state.current_page = "WelcomePage"
                st.rerun()
