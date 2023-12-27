import streamlit as st

from frontend import Tab
from frontend.utils import StUtils

class ProfileTab(Tab):

    def __init__(self):
        st.write("add email, recover password, add personality scores")
        StUtils.empty_lines(5)
        StUtils.logout_button(key="dashboard-profile-tab-logout")