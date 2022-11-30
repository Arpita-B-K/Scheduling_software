import streamlit as st
from login import show_login_page
from login import show_logout_page
from login import show_signup_page
from main import show_main_page


def main():
    st.title("TRAINING SOFTWARE")
    if 'signup' not in st.session_state:
        st.session_state['signup']=False
        st.session_state['loggedIn']=False
        show_signup_page()

    
    else:
        if st.session_state['loggedIn']:
            show_main_page()
            show_logout_page()
        else:
            show_signup_page()


if __name__ == '__main__':
    main()