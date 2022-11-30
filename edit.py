import pandas as pd
import streamlit as st
from database import view_employee_data,get_all_roles,edit_employee,edit_credentials,view_all_data,get_all_skills
from database import get_data,edit_training,get_role_id,get_all_employees,get_emp_name,Compute_full_Schedule,add_emp_schedule

def update_employee():
    menu=['Credentials','Employee']
    table=st.selectbox("Table",menu)
    result,cols=view_employee_data(table)
    df=pd.DataFrame(result,columns=cols)
    with st.expander("Current Data"):
        st.dataframe(df)

    if table=='Credentials':
        new_user_id = st.text_input(cols[0],result[0][0],disabled=True)
        new_user_name = st.text_input(cols[1],result[0][1])
        new_password = st.text_input(cols[2],result[0][2])
        new_user_type= st.text_input(cols[3],result[0][3],disabled=True)

        if st.button("Update"):
            edit_credentials(new_user_name,new_password,result[0][0])
            st.success("Successfully updated")
        
    else:
        res=get_all_roles()
        list_of_roles = [i[0] for i in res]
        new_emp_id = st.text_input(cols[0],result[0][0],disabled=True)
        new_emp_name = st.text_input(cols[1],result[0][1])
        new_skill= st.text_input(cols[2],result[0][2],disabled=True)
        new_role_id= st.text_input(cols[3],result[0][3],disabled=True)

        if st.button("Update"):
            edit_employee(new_emp_name,new_role_id,result[0][0])
            add_emp_schedule(new_emp_id)
            st.success("Successfully updated")
            
    Updated_data,col_names=view_employee_data(table)
    df=pd.DataFrame(Updated_data,columns=col_names)
    with st.expander("Updated Data"):
        st.dataframe(df)
        
def update_hr():
    menu=['Credentials','Training','Employee']
    table=st.selectbox("Table",menu)
    
    if table=='Credentials':
        result,cols=view_employee_data(table)
        df=pd.DataFrame(result,columns=cols)
        with st.expander("Current Data"):
            st.dataframe(df)

        new_user_id = st.text_input(cols[0],result[0][0],disabled=True)
        new_user_name = st.text_input(cols[1],result[0][1])
        new_password = st.text_input(cols[2],result[0][2])
        new_user_type= st.text_input(cols[3],result[0][3],disabled=True)

        if st.button("Update"):
            edit_credentials(new_user_name,new_password,result[0][0])
            st.success("Successfully updated")

        Updated_data,col_names=view_employee_data(table)
        df=pd.DataFrame(Updated_data,columns=col_names)
        with st.expander("View Updated Data"):
            st.dataframe(df)

    elif table=='Training':
        result,cols=view_all_data(table)
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)

        res=get_all_skills()
        list_of_skills = [i[0] for i in res]
        selected_skill=st.selectbox("Choose a Skill to update",list_of_skills)
        st.write(table)
        selected_result= get_data(selected_skill,table)

        list_of_scores=[0,1,2,3,4,5]
        new_skill = st.text_input(cols[0],selected_result[0][0],disabled=True)
        new_training = st.text_input(cols[1],selected_result[0][1])
        new_test= st.text_input(cols[2],selected_result[0][2])
        new_parscore = st.selectbox(cols[3],list_of_scores,list_of_scores.index(selected_result[0][3]))

        if st.button("Update"):
            edit_training(new_training,new_test,new_parscore,selected_result[0][0])
            Compute_full_Schedule()
            st.success("Successfully updated")

        updated_result,col_names=view_all_data(table)
        df=pd.DataFrame(updated_result,columns=col_names)
        with st.expander(f"View Updated Data"):
            st.dataframe(df)

    else:
        result,cols=view_all_data(table)
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)

        res=get_all_roles()
        list_of_roles = [i[0] for i in res]
        employee_list=[i[0] for i in get_all_employees()]
        e_id=st.selectbox("Select employee ID",employee_list)
        new_emp_name = st.text_input(cols[1],get_emp_name(e_id),disabled=True)
        # new_skill= st.text_input(cols[2],result[0][2],disabled=True)
        new_role_id= st.selectbox(cols[3],list_of_roles,get_role_id(e_id))

        if st.button("Update"):
            edit_employee(new_emp_name,new_role_id,e_id)
            Compute_full_Schedule()
            st.success("Successfully updated")
            
        updated_result,col_names=view_all_data(table)
        df=pd.DataFrame(updated_result,columns=col_names)
        with st.expander(f"View Updated Data"):
            st.dataframe(df)
    