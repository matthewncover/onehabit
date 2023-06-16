import streamlit as st
from datetime import date, timedelta

from .utils import Utils

class TrackerTab:

    def __init__(self):
        st.session_state.setdefault("current_date", date.today())

        self.date_navigator()
        self.habits()

    def date_navigator(self):
        _, back_col, text_col, next_col, _ = st.columns((5, 1, 2, 1, 5))

        if back_col.button("←"):
            st.session_state.current_date -= timedelta(days=1)
            st.experimental_rerun()

        date_text = st.session_state.current_date.strftime("%A, %b %d")
        text_col.write(date_text)

        if next_col.button("→"):
            st.session_state.current_date += timedelta(days=1)
            st.experimental_rerun()

    #region habits

    def habits(self):
        st.markdown("##### Habits")

        

    #endregion
    #region observations

    #endregion