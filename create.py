import streamlit as st
import pandas as pd
from database import add_to_training,view_all_data,add_to_job,get_all_skills,Compute_full_Schedule,delete_schedule

def add():
    menu=['training','job']
    table=st.selectbox("Select Table",menu)

    result,cols=view_all_data(table)
    df=pd.DataFrame(result,columns=cols)
    with st.expander(f"View {table}"):
        st.dataframe(df)

    if table=='training':
        list_of_scores=[0,1,2,3,4,5]
        new_skill = st.text_input("Skill")
        new_training = st.text_input("Training_course")
        new_test= st.text_input("Test")
        new_parscore = st.selectbox("Parscore",list_of_scores)

        if st.button("Add"):
            add_to_training(new_skill,new_training,new_test,new_parscore)
            st.success("Successfully added")

    else:
        res=get_all_skills()
        list_of_skills = [i[0] for i in res]
        role_id=st.text_input("Role id")
        role_name=st.text_input("Role Name")
        skill=st.selectbox("Skill Required",list_of_skills)

        if st.button("Add"):
            add_to_job(role_id,role_name,skill)
            Compute_full_Schedule()
            st.success("Successfully added")
            # st.success("Successfully updated Schedule")
            #Schedule Changes

    new_result,new_cols=view_all_data(table)
    df=pd.DataFrame(new_result,columns=new_cols)
    with st.expander(f"View Updated {table}"):
        st.dataframe(df)










