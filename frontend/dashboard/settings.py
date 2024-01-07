import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class SettingsTab(Tab):

    def __init__(self):
        options_col, _, content_col = st.columns((1, .5, 3))

        subtab = options_col.radio(" ", options=["profile", "coach settings", "feedback"])
        options_col.divider()

        with content_col:
            getattr(self, f"_{subtab.replace(' ', '_')}_subtab")()

        StUtils.empty_lines(5)

    def _profile_subtab(self):
        st.write("profile")
        st.write("update email")
        st.write("save")

    def _coach_settings_subtab(self):
        st.write("personality options")

    def _feedback_subtab(self):
        st.write("feedback form")
        st.write("sanitize inputs")
        st.write("limit to one per day per user")