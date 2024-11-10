create database companyDB;

use companyDB;

create table user(
	user_id  int auto_increment primary key ,
	user_name  varchar(50)  not null unique,
	user_password varchar(50)  not null,
	user_type enum("Employee","Admin","Manager")
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
CREATE TABLE manager (
    manager_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE admin (
    admin_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
create table task
(
 taskID  int unique primary key not null,
 task_name varchar(50) not null,
 deskripsi text null,
 id_employee int not null,
 foreign key(id_employee) references employee(employee_id)
);


create table project
(
	ProjectID  int unique primary key not null,
	Project_name varchar(50) not null,
	manager_id int not null,
	foreign key(manager_id) references manager(manager_id)
);


insert into user(user_name,user_password,user_type)
value("test1","1234","Employee"),
value("test1","1234","Employee"),
value("test1","1234","Employee");

select e.employee_id from employee e
join user u on u.user_id = e.employee_id ;


