create database companyDB;

use companyDB;

create table user(
	userid  int auto_increment primary key ,
	username  varchar(50)  not null unique,
	userpassword varchar(50)  not null,
    usertype enum('Employee','Admin','Manager')
);

CREATE TABLE employee (
    employeeid INT PRIMARY KEY auto_increment,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);
CREATE TABLE manager (
    managerid INT PRIMARY KEY auto_increment,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);

CREATE TABLE admin (
    adminid INT PRIMARY KEY auto_increment,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);


create table project
(
	projectid  int primary key auto_increment,
	projectname varchar(50) not null,
	managerid int not null,
    projectstatus enum('Not Done', 'Done') not null default 'Not Done',
	foreign key(managerid) references manager(managerid)
);

create table task
(
 taskid  int primary key auto_increment,
 taskname varchar(50) not null,
 deskripsi text null,
 employeeid int not null,
 projectid int not null,
 taskdue date ,
 status enum('Not Done', 'Done') not null default 'Not Done',
 foreign key (projectid) references project(projectid),
 foreign key (employeeid) references employee(employeeid)
);

-- Insert sample data into user table
INSERT INTO user (username, userpassword, usertype) VALUES 
('john_doe', 'password123', 'Employee'),
('jane_smith', 'password456', 'Manager'),
('admin_user', 'adminpass', 'Admin');

-- Insert sample data into employee table
INSERT INTO employee (userid) VALUES 
((SELECT userid FROM user WHERE username = 'john_doe'));

-- Insert sample data into manager table
INSERT INTO manager (userid) VALUES 
((SELECT userid FROM user WHERE username = 'jane_smith'));

-- Insert sample data into admin table
INSERT INTO admin (userid) VALUES 
((SELECT userid FROM user WHERE username = 'admin_user'));

-- Insert sample data into project table
INSERT INTO project (Projectname, managerid) VALUES 
('Project Alpha', (SELECT managerid FROM manager m JOIN user u ON m.userid = u.userid WHERE u.username = 'jane_smith'));

-- Insert sample data into task table
INSERT INTO task (taskname, deskripsi, idemployee, projectid) VALUES 
('Task 1', 'Description for Task 1', (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'john_doe'), (SELECT projectid FROM project WHERE Projectname = 'Project Alpha'));

select e.employeeid from employee e
join user u on u.userid = e.userid;


-- additional sample data


-- Insert more sample data into user table
INSERT INTO user (username, userpassword, usertype) VALUES 
('alice_jones', 'alicepass', 'Employee'),
('bob_brown', 'bobspassword', 'Employee'),
('charlie_manager', 'charlie123', 'Manager'),
('david_admin', 'davidadmin', 'Admin');

-- Insert more sample data into employee table
INSERT INTO employee (userid) VALUES 
((SELECT userid FROM user WHERE username = 'alice_jones')),
((SELECT userid FROM user WHERE username = 'bob_brown'));

-- Insert more sample data into manager table
INSERT INTO manager (userid) VALUES 
((SELECT userid FROM user WHERE username = 'charlie_manager'));

-- Insert more sample data into admin table
INSERT INTO admin (userid) VALUES 
((SELECT userid FROM user WHERE username = 'david_admin'));

-- Insert more sample data into project table
INSERT INTO project (projectname, managerid) VALUES 
('Project Beta', (SELECT managerid FROM manager m JOIN user u ON m.userid = u.userid WHERE u.username = 'jane_smith')),
('Project Gamma', (SELECT managerid FROM manager m JOIN user u ON m.userid = u.userid WHERE u.username = 'charlie_manager'));

-- Insert more sample data into task table
INSERT INTO task (taskname, deskripsi, employeeid, projectid, taskdue, status) VALUES 
('Task 2', 'Description for Task 2', (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'alice_jones'), (SELECT projectid FROM project WHERE projectname = 'Project Beta'), CURRENT_DATE + INTERVAL 5 DAY, 'Not Done'),
('Task 3', 'Description for Task 3', (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'bob_brown'), (SELECT projectid FROM project WHERE projectname = 'Project Gamma'), CURRENT_DATE + INTERVAL 10 DAY, 'Not Done'),
('Task 4', 'Description for Task 4', (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'john_doe'), (SELECT projectid FROM project WHERE projectname = 'Project Alpha'), CURRENT_DATE + INTERVAL 3 DAY, 'Done');
