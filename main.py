import streamlit as st
from read import view
from database import get_user_type
from database import get_user_id
from database import Compute_full_Schedule
from edit import update_employee
from edit import update_hr
from test import Take_test
from create import add
from delete import delete
from Notification import Notify_employee,Notify_hr

def get_menu(user_type):
    if user_type=='employee':
        menu=['View','Update','Take Test','Notifications']
    else:
        menu=['Add','View','Update','Delete','Notifications']
    
    return menu

def show_main_page():
        
    user_id=get_user_id()
    user_type=get_user_type()
    menu = get_menu(user_type)
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add":
        st.subheader("Add")
        add()
    if choice == "View":
        st.subheader("View:")
        view()
    if choice=="Update" and user_type=='employee':
        st.subheader("Update")
        update_employee()
    if choice=="Update" and user_type=='hr':
        st.subheader("Update")
        update_hr()
    if choice=="Delete":
        st.subheader("Delete")
        delete()
    if choice=="Take Test":
        st.subheader("Test")
        Take_test()
    if choice=='Notifications' and user_type=='employee':
        st.subheader("Notifications")
        Notify_employee()
    if choice=='Notifications' and user_type=='hr':
        st.subheader("Notifications")
        Notify_hr()
    else:
        pass
