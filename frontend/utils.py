import streamlit as st

class Utils:

    @staticmethod
    def back_button(page:str):
        back = st.button("Back")
        if back:
            st.session_state.current_page = page
            st.experimental_rerun()

    @staticmethod
    def logout_button():
        logout = st.button("logout")
        if logout:
            st.session_state.current_page = "LoginPage"
            st.experimental_rerun()
    
    @staticmethod
    def empty_lines(n=1):
        st.markdown("<br>"*n, unsafe_allow_html=True)
    
    @staticmethod
    def not_implemented():
        st.write("Not Implemented")