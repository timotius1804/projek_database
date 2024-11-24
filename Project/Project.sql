-- Buat database jika belum ada
CREATE DATABASE IF NOT EXISTS companyDB;

-- Gunakan database tersebut
USE companyDB;

-- Buat tabel user
CREATE TABLE IF NOT EXISTS user (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    userpassword VARCHAR(50) NOT NULL,
    usertype ENUM('Employee', 'Admin', 'Manager')
);

-- Buat tabel employee
CREATE TABLE IF NOT EXISTS employee (
    employeeid INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);

-- Buat tabel manager
CREATE TABLE IF NOT EXISTS manager (
    managerid INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);

-- Buat tabel admin
CREATE TABLE IF NOT EXISTS admin (
    adminid INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(userid)
);

-- Buat tabel project
CREATE TABLE IF NOT EXISTS project (
    projectid INT AUTO_INCREMENT PRIMARY KEY,
    projectname VARCHAR(50) NOT NULL,
    managerid INT NOT NULL,
    projectstatus ENUM('Not Done', 'Done') NOT NULL DEFAULT 'Not Done',
    FOREIGN KEY (managerid) REFERENCES manager(managerid)
);

-- Buat tabel task
CREATE TABLE IF NOT EXISTS task (
    taskid INT AUTO_INCREMENT PRIMARY KEY,
    taskname VARCHAR(50) NOT NULL,
    deskripsi TEXT NULL,
    employeeid INT NOT NULL,
    projectid INT NOT NULL,
    taskdue DATE,
    status ENUM('Not Done', 'Done') NOT NULL DEFAULT 'Not Done',
    FOREIGN KEY (projectid) REFERENCES project(projectid),
    FOREIGN KEY (employeeid) REFERENCES employee(employeeid)
);

-- Masukkan data contoh ke tabel user
INSERT INTO user (username, userpassword, usertype) VALUES 
('john_doe', 'password123', 'Employee'),
('jane_smith', 'password456', 'Manager'),
('admin_user', 'adminpass', 'Admin');

-- Masukkan data contoh ke tabel employee
INSERT INTO employee (userid) 
VALUES ((SELECT userid FROM user WHERE username = 'john_doe'));

-- Masukkan data contoh ke tabel manager
INSERT INTO manager (userid) 
VALUES ((SELECT userid FROM user WHERE username = 'jane_smith'));

-- Masukkan data contoh ke tabel admin
INSERT INTO admin (userid) 
VALUES ((SELECT userid FROM user WHERE username = 'admin_user'));

-- Masukkan data contoh ke tabel project
INSERT INTO project (projectname, managerid) 
VALUES ('Project Alpha', (SELECT managerid FROM manager m JOIN user u ON m.userid = u.userid WHERE u.username = 'jane_smith'));

-- Masukkan data contoh ke tabel task
INSERT INTO task (taskname, deskripsi, employeeid, projectid) 
VALUES ('Task 1', 'Description for Task 1', 
        (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'john_doe'), 
        (SELECT projectid FROM project WHERE projectname = 'Project Alpha'));
