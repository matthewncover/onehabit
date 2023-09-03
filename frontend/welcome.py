import streamlit as st

from . import Page
from .utils import Utils

class WelcomePage(Page):

    def __init__(self):
        super().__init__()
        Utils.not_implemented()