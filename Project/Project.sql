create database companyDB;

use companyDB;

create table user(
	user_id  int auto_increment primary key ,
	user_name  varchar(50)  not null unique,
	user_password varchar(50)  not null,
    user_type enum('Employee','Admin','Manager')
);

CREATE TABLE employee (
    employee_id INT PRIMARY KEY auto_increment,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
CREATE TABLE manager (
    manager_id INT PRIMARY KEY auto_increment,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE admin (
    admin_id INT PRIMARY KEY auto_increment,
    user_id INT NOT NULL,
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
 status enum('Not Done', 'Done') not null default 'Not Done',
 foreign key (project_id) references project(ProjectID),
 foreign key (id_employee) references employee(employee_id)
);

-- Insert sample data into user table
INSERT INTO user (user_name, user_password, user_type) VALUES 
('john_doe', 'password123', 'Employee'),
('jane_smith', 'password456', 'Manager'),
('admin_user', 'adminpass', 'Admin');

-- Insert sample data into employee table
INSERT INTO employee (user_id) VALUES 
((SELECT user_id FROM user WHERE user_name = 'john_doe'));

-- Insert sample data into manager table
INSERT INTO manager (user_id) VALUES 
((SELECT user_id FROM user WHERE user_name = 'jane_smith'));

-- Insert sample data into admin table
INSERT INTO admin (user_id) VALUES 
((SELECT user_id FROM user WHERE user_name = 'admin_user'));

-- Insert sample data into project table
INSERT INTO project (Project_name, manager_id) VALUES 
('Project Alpha', (SELECT manager_id FROM manager m JOIN user u ON m.user_id = u.user_id WHERE u.user_name = 'jane_smith'));

-- Insert sample data into task table
INSERT INTO task (task_name, deskripsi, id_employee, project_id) VALUES 
('Task 1', 'Description for Task 1', (SELECT employee_id FROM employee e JOIN user u ON e.user_id = u.user_id WHERE u.user_name = 'john_doe'), (SELECT ProjectID FROM project WHERE Project_name = 'Project Alpha'));

select e.employee_id from employee e
join user u on u.user_id = e.user_id;


