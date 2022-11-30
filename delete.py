import pandas as pd
import streamlit as st
from database import view_all_data,get_all_skills,delete_training,delete_job,delete_employee,get_all_employees
from database import Compute_full_Schedule

def delete():
    menu=['training','job','employee']
    table=st.selectbox("Select Table",menu)

    result,cols=view_all_data(table)
    df=pd.DataFrame(result,columns=cols)
    with st.expander(f"View {table}"):
        st.dataframe(df)

    if table=='employee':
        employee_list=[i[0] for i in get_all_employees()]
        selected_employee=st.selectbox("Select employee id to delete",employee_list)

        if st.button("Delete"):
            delete_employee(selected_employee)
            st.success("Successfully Deleted")

    else:
        rows=[result[i] for i in range(len(result))]
        selected_row=st.selectbox("Select data to be deleted",rows)

        if st.button("Delete"):
            if table=='training':
                delete_training(selected_row[0])
                Compute_full_Schedule()
            else:
                delete_job(selected_row)
                Compute_full_Schedule()
                
            st.success("Successfully Deleted")


    new_result,new_cols=view_all_data(table)
    df=pd.DataFrame(new_result,columns=new_cols)
    with st.expander(f"View Updated {table}"):
        st.dataframe(df)

    # if table=='training':
    #     skill_list=[i[0] for i in get_all_skills()]
    #     selected_skill=st.selectbox("Select a skill to delete",skill_list)

    #     if st.button("Delete"):
    #         delete_training(selected_skill)
    #         st.success("Successfully Deleted")

    # elif table=='job':