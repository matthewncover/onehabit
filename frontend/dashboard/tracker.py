import streamlit as st
from datetime import date, timedelta

from frontend import Tab
from frontend.utils import StUtils

class TrackerTab(Tab):

    def __init__(self):
        super().__init__()
        st.session_state.setdefault("current_date", date.today())

        self.date_navigator()
        self.habits()

    def date_navigator(self):
        _, back_col, text_col, next_col, _ = st.columns((5, 1, 3, 1, 5))

        if back_col.button("←"):
            st.session_state.current_date -= timedelta(days=1)
            st.rerun()

        date_text = st.session_state.current_date.strftime("%A, %b %d")
        text_col.write(date_text)

        if next_col.button("→"):
            st.session_state.current_date += timedelta(days=1)
            st.rerun()

    #region habits

    def habits(self):
        st.markdown("##### Habits")

        

    #endregion
    #region observations

    #endregion