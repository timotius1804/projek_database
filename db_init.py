def db_init(cursor, db):
    cursor.execute("CREATE DATABASE IF NOT EXISTS companyDB")
    cursor.execute("USE companyDB")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        userid INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        userpassword VARCHAR(50) NOT NULL,
        usertype ENUM('Employee', 'Admin', 'Manager')
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        employeeid INT AUTO_INCREMENT PRIMARY KEY,
        userid INT NOT NULL,
        FOREIGN KEY (userid) REFERENCES user(userid)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS manager (
        managerid INT AUTO_INCREMENT PRIMARY KEY,
        userid INT NOT NULL,
        FOREIGN KEY (userid) REFERENCES user(userid)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        adminid INT AUTO_INCREMENT PRIMARY KEY,
        userid INT NOT NULL,
        FOREIGN KEY (userid) REFERENCES user(userid)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        projectid INT AUTO_INCREMENT PRIMARY KEY,
        projectname VARCHAR(50) NOT NULL,
        managerid INT NOT NULL,
        projectstatus ENUM('Not Done', 'Done') NOT NULL DEFAULT 'Not Done',
        FOREIGN KEY (managerid) REFERENCES manager(managerid)
    )
    """)
    
    cursor.execute("""
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
    )
    """)
    
    # Insert sample data into user table
    cursor.execute("""
    INSERT INTO user (username, userpassword, usertype) VALUES 
    ('john_doe', 'password123', 'Employee'),
    ('jane_smith', 'password456', 'Manager'),
    ('admin_user', 'adminpass', 'Admin')
    """)
    
    # Insert sample data into employee table
    cursor.execute("""
    INSERT INTO employee (userid) VALUES 
    ((SELECT userid FROM user WHERE username = 'john_doe'))
    """)
    
    # Insert sample data into manager table
    cursor.execute("""
    INSERT INTO manager (userid) VALUES 
    ((SELECT userid FROM user WHERE username = 'jane_smith'))
    """)
    
    # Insert sample data into admin table
    cursor.execute("""
    INSERT INTO admin (userid) VALUES 
    ((SELECT userid FROM user WHERE username = 'admin_user'))
    """)
    
    # Insert sample data into project table
    cursor.execute("""
    INSERT INTO project (projectname, managerid) VALUES 
    ('Project Alpha', (SELECT managerid FROM manager m JOIN user u ON m.userid = u.userid WHERE u.username = 'jane_smith'))
    """)
    
    # Insert sample data into task table
    cursor.execute("""
    INSERT INTO task (taskname, deskripsi, employeeid, projectid) VALUES 
    ('Task 1', 'Description for Task 1', (SELECT employeeid FROM employee e JOIN user u ON e.userid = u.userid WHERE u.username = 'john_doe'), (SELECT projectid FROM project WHERE projectname = 'Project Alpha'))
    """)
    
    db.commit()