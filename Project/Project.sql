create database companyDB;

use companyDB;

create table user(
	user_id  int auto_increment primary key ,
	user_name  varchar(50)  not null unique,
	user_password varchar(50)  not null,
	user_type enum("Employee","Admin","Manager")
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY auto_increment,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
CREATE TABLE manager (
    manager_id INT PRIMARY KEY auto_increment,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE admin (
    admin_id INT PRIMARY KEY auto_increment,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);


create table project
(
	ProjectID  int primary key auto_increment,
	Project_name varchar(50) not null,
	manager_id int not null,
	foreign key(manager_id) references manager(manager_id)
);

create table task
(
 taskID  int primary key auto_increment,
 task_name varchar(50) not null,
 deskripsi text null,
 id_employee int not null,
 project_id int not null,
 foreign key (project_id) references project(ProjectID)
 foreign key (id_employee) references employee(employee_id)
);



select e.employee_id from employee e
join user u on u.user_id = e.employee_id ;


