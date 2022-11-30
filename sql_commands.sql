create database Training_software;

use database Training_software;

-- credentials(user_id,name,password,user_type)
-- -- user_logs(user_name,password,login_date,login_time,logout_time)
-- job(role_id,role_name,skills_required)
-- employee(emp_id,name,role_id,skillset)
-- training(skill,training,test,parscore)  
-- schedule(emp_id,training,start_date,end_date,test)#status

create table credentials(user_id int,name varchar(30),password varchar(30) not null,user_type varchar(10) ,check(user_type in ('employee','hr')),primary key(user_id));
create table job(role_id int ,role_name varchar(30),skills_required varchar(30),primary key(role_id,skills_required));
create table employee(emp_id int,emp_name varchar(30),skills varchar(30),role_id int,primary key(emp_id,role_id,skills));
create table training(skill varchar(30),training varchar(50) not null,test varchar(30),parscore int,primary key(skill));
create table schedule(emp_id int,training varchar(50),start_date date,end_date date,test varchar(30),primary key(emp_id,training));
create table hr_notification(u_name varchar(30),skill varchar(255),notification_type varchar(15),check(notification_type in ('add_employee','add_schedule')));

alter table job add foreign key(skills_required) references training(skill) on delete cascade;
alter table employee add foreign key(skills) references training(skill) on delete cascade;
alter table employee add foreign key(role_id) references job(role_id) on delete cascade;
alter table schedule add foreign key(emp_id) references employee(emp_id) on delete cascade;
alter table employee add foreign key(role_id) references job(role_id) on update cascade;
alter table schedule add foreign key(emp_id) references employee(emp_id) on update cascade;

insert into credentials values(2,'Ajith S','Ashokde0314','employee');
insert into credentials values(3,'Hitesh','hitesh','employee');
insert into credentials values(4,'Arpitha','arpitha','employee');
insert into credentials values(5,'Geerish','geerish','employee');
insert into credentials values(1,'Anand Subbarao','anandpes','hr');

insert into training values('MongoDB','MongoCourse','MongoTest',4);
insert into training values('Java','CoreJavaCourse','JavaTest',3);
insert into training values('React','ReactCourse','ReactTest',4);
insert into training values('Java Script','JSCourse','JSTest',4);
insert into training values('Python','PythonCourse','PythonTest',5);
insert into training values('C','C Programming Course','CTest',4);
insert into training values('R','R Programming for Data SCience Course','RTest',4);

insert into job values(2,"Web Developer","MongoDB");
insert into job values(1,"Developer","Java");
insert into job values(1,"Developer",'C');
insert into job values(2,"Web Developer","React");
insert into job values(2,"Web Developer","Java Script");
insert into job values(3,"Bussiness Analyst","Python");
insert into job values(3,"Bussiness Analyst","R");

insert into employee values(2,'Ajith S','C',1);
insert into employee values(2,'Ajith S','Python',1);
insert into employee values(2,'Ajith S','React',1);
insert into employee values(3,'Hitesh','C',2);
insert into employee values(3,'Hitesh','Python',2);
insert into employee values(3,'Hitesh','React',2);
insert into employee values(3,'Hitesh','Java Script',2);
insert into employee values(4,'Arpitha','Python',3);
insert into employee values(5,'Geerish','C',1);





