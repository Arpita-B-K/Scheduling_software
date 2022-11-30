import streamlit as st
from database import Authenticate
from database import add_credential,get_all_skills,add_hr_notification


def show_login_page():
    if st.session_state['loggedIn']==False:
        user_id=st.text_input(label="",value="",placeholder="User ID")  
        password=st.text_input(label="",value="",placeholder="Password",type="password")
        st.session_state['u_id']=user_id
        st.button("Login",on_click=login_clicked,args=(user_id,password))

def show_signup_page():
    if st.session_state['signup']==False:
        # u_id=st.text_input(label="",value="",placeholder="User ID")  
        user_name=st.text_input(label="",value="",placeholder="Name")  
        passcode=st.text_input(label="",value="",placeholder="Password",type="password")
        user_type='employee'
        # list_of_skills = [i[0] for i in get_all_skills()]
        # skill_set=st.multiselect('skillset',list_of_skills)
        skill_set=st.text_area(label='',value='',placeholder="Enter your skill description")

        if st.button("Signup"):
            add_credential(user_name,passcode,user_type)
            add_hr_notification(user_name,skill_set)
            st.session_state['signup']=True

        if st.button('Signin'):
            st.session_state['signup']=True
    else:
        show_login_page()

def login_clicked(user_id,password):
    var=Authenticate(user_id,password)
    # var=True
    if var:
        st.session_state['loggedIn']=True
        
    else:
        st.session_state['loggedIn']==False
        st.error("Invalid User")

def show_logout_page():
    st.button("LogOut",on_click=LogOut_Clicked)

def LogOut_Clicked():
    st.session_state['loggedIn']=False



    

