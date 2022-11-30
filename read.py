import streamlit as st
import pandas as pd
from database import get_user_type
from database import view_employee_data
from database import view_all_data
from database import get_user_id
from database import Compute_full_Schedule
# from database import Compute_emp_Schedule
from database import get_emp_schedule
from database import get_full_schedule




def view_access():
    # user_id=get_user_id()
    u_id=get_user_id()
    user_type=get_user_type()

    if user_type=='employee':
        view_menu=['Credentials','Employee','Schedule']
    else:
        view_menu=['Credentials','Training','Job','Schedule']

    return view_menu

def view():
    view_menu=view_access()
    table=st.selectbox(label='',options=view_menu)

    if table=='Schedule' and get_user_type()=='employee':
        u_id=get_user_id()
        result,cols=get_emp_schedule(u_id)
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)

    elif table=='Schedule' and get_user_type()=='hr':
        # result=Compute_full_Schedule()
        result,cols=get_full_schedule()
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)

    elif get_user_type()=='employee' or table=='Credentials':
        result,cols=view_employee_data(table)
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)

    else:
        result,cols=view_all_data(table)
        df=pd.DataFrame(result,columns=cols)
        with st.expander(f"View {table}"):
            st.dataframe(df)
    