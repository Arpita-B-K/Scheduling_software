import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Training_Software"
)
c = mydb.cursor()

def Authenticate(u_id,passcode):
    c.execute(f'select password from credentials where user_id="{u_id}"')
    data=c.fetchall()
    if data:
        if data[0][0]==passcode:
            return True
        else:
            return False
    else:
        return False

def get_user_id():
    return st.session_state['u_id']

def get_user_type():
    u_id=get_user_id()
    c.execute(f"select user_type from credentials where user_id='{u_id}'")
    data=c.fetchall()
    return data[0][0]

def view_employee_data(tab):
    u_id=get_user_id()
    c.execute(f"show keys from {tab} where key_name='primary'")
    data=c.fetchall()
    key=data[0][4]
    c.execute(f"select * from {tab} where {key}={u_id}")
    res=c.fetchall()
    return res,c.column_names


def view_all_data(tab):
    c.execute(f"select * from {tab}")
    data=c.fetchall()
    return data,c.column_names

def get_all_roles():
    c.execute('select distinct(role_id) from job')
    data=c.fetchall()
    return data

def get_all_skills():
    c.execute('select skill from training')
    data=c.fetchall()
    return data

def edit_employee(new_emp_name,new_role_id,e_id):
    c.execute("update employee set emp_name=%s,role_id=%s where emp_id=%s ",(new_emp_name,new_role_id,e_id))
    mydb.commit()

def edit_credentials(new_user_name,new_password,u_id):
    c.execute("update credentials set name=%s,password=%s where user_id=%s",(new_user_name,new_password,u_id))
    mydb.commit()

def edit_training(new_training,new_test,new_parscore,pk):
    c.execute("update training set training=%s,test=%s,parscore=%s where skill=%s",(new_training,new_test,new_parscore,pk))
    mydb.commit()

def get_data(pk,tab):
    c.execute(f"show keys from {tab} where key_name='primary'")
    data=c.fetchall()
    key=data[0][4]
    c.execute(f"select * from {tab} where {key}='{pk}'")
    res=c.fetchall()
    return res

def add_to_training(new_skill,new_training,new_test,new_parscore):
    c.execute('insert into training values(%s,%s,%s,%s)',(new_skill,new_training,new_test,new_parscore))
    mydb.commit()

def add_to_job(role_id,role_name,skill):
    c.execute('insert into job values(%s,%s,%s)',(role_id,role_name,skill))
    mydb.commit()

def delete_training(pk):
    c.execute(f"delete from training where skill='{pk}'")
    mydb.commit()

def delete_job(row):
    c.execute(f"delete from job where role_id={row[0]} and role_name='{row[1]}' and skills_required='{row[2]}'")
    mydb.commit()

def get_all_employees():
    c.execute('select distinct(emp_id) from employee')
    data=c.fetchall()
    return data

def delete_employee(e_id):
    c.execute(f'delete from credentials where user_id={e_id}')
    c.execute(f"delete from employee where emp_id={e_id}")
    c.execute(f"delete from schedule where emp_id={e_id}")
    mydb.commit()

def get_role_id(e_id):
    c.execute(f'select distinct(role_id) from employee where emp_id={e_id}')
    data=c.fetchall()
    return data[0][0]

def get_emp_name(e_id):
    c.execute(f'select distinct(emp_name) from employee where emp_id={e_id}')
    data=c.fetchall()
    return data[0][0]

def get_schedule_skill(e_id):
    r_id=get_role_id(e_id)
    c.execute(f'select skills_required from job where role_id={r_id}')
    skills_required=c.fetchall()
    c.execute(f'select skills from employee where emp_id={e_id}')
    skillset=c.fetchall()

    list_of_skills_required=[i[0] for i in skills_required]
    list_of_skillset=[i[0] for i in skillset]

    result=[]
    for skill in list_of_skills_required:
        if skill not in list_of_skillset:
            result.append(skill)

    return result

def get_skill_training_test(skill_list):
    # skill_tuple=tuple(skill_list)
    res=[]
    for skill in skill_list:
        c.execute(f"select training,test from training where skill='{skill}'")
        data=c.fetchall()
        res.append([data[0][0],data[0][1]])
    return res

def get_skill_training(skill_list):
    # skill_tuple=tuple(skill_list)
    res=[]
    for skill in skill_list:
        c.execute(f"select training from training where skill='{skill}'")
        data=c.fetchall()
        res.append(data[0][0])
    return res


def Compute_emp_schedule(e_id):
    skill=get_schedule_skill(e_id)
    training=get_skill_training_test(skill)

    emp_schedule=[]
    for course in training:
        emp_schedule.append([e_id,course[0],course[1]])

    return emp_schedule

def Compute_full_Schedule():
    delete_schedule()
    list_of_emp_id=[i[0] for i in get_all_employees()]

    frames=[]
    for emp_id in list_of_emp_id:
        emp_schedule=Compute_emp_schedule(emp_id)
        for row in emp_schedule:
            insert_emp_schedule(row)
    #     df=pd.DataFrame(emp_schedule)
    #     frames.append(df)

    # result = pd.concat(frames)
    
    # return result  

def delete_schedule():
    c.execute('delete from schedule')
    mydb.commit()

def add_credential(u_name,passcode,u_type):
    try :
        c.execute('insert into credentials(name,password,user_type) values(%s,%s,%s)',(u_name,passcode,u_type))
        mydb.commit()
    except :
        pass
    
def update_credential(emp_id,emp_name):
    c.execute('update credentials set user_id=%s where name=%s',(emp_id,emp_name))
    mydb.commit()

def add_hr_notification(u_name,skillset):
    # for skill in skillset:
    try:
        c.execute("insert into hr_notification values(%s,%s)",(u_name,skillset))
        mydb.commit()
    except:
        pass

def get_notifications():
    c.execute("select * from hr_notification ")
    data=c.fetchall()
    return data

def get_par_score(course):
    c.execute(f"select skill,parscore from training where training='{course}'")
    score=c.fetchall()
    return score[0][0],score[0][1]

def add_employee(e_id,e_name,skillset,r_id):
    for skill in skillset:
        c.execute('insert into employee values(%s,%s,%s,%s)',(e_id,e_name,skill,r_id))
        mydb.commit()
    
def delete_hr_notification(emp_name):
    c.execute(f'delete from hr_notification where u_name="{emp_name}"')
    mydb.commit()


def update_emp_skill(u_id,skill):
    c.execute(f"select emp_name,role_id from employee where emp_id = {u_id}")
    data=c.fetchall()
    (name , role) = (data[0][0],data[0][1])
    c.execute("insert into employee values(%s,%s,%s,%s)",(u_id,name,skill,role))
    mydb.commit()

def get_full_schedule():
    c.execute("select * from Schedule where start_date not in ('NULL')")
    data=c.fetchall()
    return data,c.column_names

def get_emp_schedule(e_id):
    c.execute(f"select * from Schedule where emp_id={e_id}")
    data=c.fetchall()
    return data,c.column_names

def get_null_schedule():
    c.execute("select * from schedule where start_date is NULL")
    data=c.fetchall()
    return data,c.column_names

def get_all_courses():
    c.execute('select distinct(training) from training')
    data=c.fetchall()
    return data

def add_dates(e_id,course,s_date,e_date):
    c.execute('update schedule set start_date=%s , end_date=%s where emp_id=%s and training=%s',(s_date,e_date,e_id,course))
    mydb.commit()

def insert_emp_schedule(row):
    c.execute('insert into schedule(emp_id,training,test) values(%s,%s,%s)',(row[0],row[1],row[2]))
    mydb.commit()

def add_emp_schedule(emp_id):
    c.execute(f"delete from schedule where emp_id={emp_id}")
    emp_schedule=Compute_emp_schedule(emp_id)
    for row in emp_schedule:
            insert_emp_schedule(row)

def new_emp_id():
    try:
        c.execute('select max(emp_id) from employee')
        data=c.fetchall()
        return data[0][0]+1
    except:
        return 2

def delete_emp_schedule(e_id,course):
    c.execute('delete from schedule where emp_id=%s and training=%s',(e_id,course))
    mydb.commit()

def delete_from_credentials(emp_name):
    c.execute(f'delete from credentials where name="{emp_name}"')
    mydb.commit()

def get_courses(e_id):
    c.execute(f"select training from schedule where emp_id='{e_id}'")
    data=c.fetchall()
    return data

def remove_schedule(e_id,course):
    c.execute("delete from schedule where emp_id=%s and training=%s",(e_id,course))
    mydb.commit()
    
