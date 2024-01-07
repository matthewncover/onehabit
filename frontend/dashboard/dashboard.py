import streamlit as st

from . import DashboardTabs
from frontend.utils import StUtils

class UserDashboardPage:

    def __init__(self):
        _, col, _ = st.columns((1, 3, 1))

        tab_names = [x.name for x in DashboardTabs][:-1] + ["..."]
        tab_classes = [x.value for x in DashboardTabs]

        with col:
            StUtils.display_tabs(tab_names, tab_classes)