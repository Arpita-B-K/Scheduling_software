import streamlit as st
import pandas as pd
from database import get_notifications,get_all_roles,get_all_skills,add_employee,delete_hr_notification,get_null_schedule
from database import get_all_employees,get_all_courses,add_dates,add_emp_schedule,new_emp_id,update_credential,delete_emp_schedule
from database import delete_from_credentials
from datetime import date,timedelta

def Notify_employee():
    pass


def Notify_hr():
    choice=st.selectbox(label='',options=['add_employee','add_schedule'])
    if choice=='add_employee':
        data=get_notifications()
        notifications=pd.DataFrame(data,columns=['user_name','skill'])
        with st.expander('view notifications'):
            st.dataframe(notifications)

        res_roles=get_all_roles()
        list_of_roles = [i[0] for i in res_roles]
        emp_id = st.text_input(label='Employee_id',value=new_emp_id())
        emp_name = st.text_input('User_Name')
        role_id= st.selectbox("Role_id",list_of_roles)
        res_skills=get_all_skills()
        list_of_skills = [i[0] for i in res_skills]
        skill=st.multiselect("Skill",list_of_skills)

        if st.button("Add Employee"):
            add_employee(emp_id,emp_name,skill,role_id)
            update_credential(emp_id,emp_name)
            delete_hr_notification(emp_name)
            #Notify Employee You are been assigned a role of {role_name}
            add_emp_schedule(emp_id)
            st.success("Succesfully Added")

        if st.button("Reject Employee"):
            delete_from_credentials(emp_name)
            delete_hr_notification(emp_name)
    
    else:
        result,cols=get_null_schedule()
        df=pd.DataFrame(result,columns=cols)
        with st.expander('view notifications'):
            st.dataframe(df)

        employee_list=[i[0] for i in get_all_employees()]
        e_id=st.selectbox("Select employee ID",employee_list)
        course_list=[i[0] for i in get_all_courses()]
        course=st.selectbox("Select Course",course_list)
        s_date_max=date.today()+ timedelta(days=10)
        e_date_max=s_date_max+timedelta(days=30)
        start_date=st.date_input('Start Date',min_value=date.today(),max_value=s_date_max)
        end_date=st.date_input('End Date',value=s_date_max,min_value=s_date_max,max_value=e_date_max)

        if st.button('Approve Schedule'):
            add_dates(e_id,course,start_date,end_date)
            #Notify Employee - Your schedule has been approved all the best for training
            st.success('Schedule Approved')

        # if st.button('Disaprove'):
        #     delete_emp_schedule(e_id,course)