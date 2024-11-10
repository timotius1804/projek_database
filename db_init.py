def db_init(cursor, db):
    cursor.execute("CREATE DATABASE IF NOT EXISTS companyDB")
    cursor.execute("USE companyDB")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(50) NOT NULL UNIQUE,
        user_password VARCHAR(50) NOT NULL,
        user_type ENUM('Employee', 'Admin', 'Manager')
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS manager (
        manager_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        ProjectID INT AUTO_INCREMENT PRIMARY KEY,
        Project_name VARCHAR(50) NOT NULL,
        manager_id INT NOT NULL,
        FOREIGN KEY (manager_id) REFERENCES manager(manager_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task (
        taskID INT AUTO_INCREMENT PRIMARY KEY,
        task_name VARCHAR(50) NOT NULL,
        deskripsi TEXT NULL,
        id_employee INT NOT NULL,
        project_id INT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES project(ProjectID),
        FOREIGN KEY (id_employee) REFERENCES employee(employee_id)
    )
    """)
    
    # Insert sample data into user table
    cursor.execute("""
    INSERT INTO user (user_name, user_password, user_type) VALUES 
    ('employee', '1234', 'Employee'),
    ('manager', '1234', 'Manager'),
    ('admin', '1234', 'Admin')
    """)
    
    # Insert sample data into employee table
    cursor.execute("""
    INSERT INTO employee (user_id) VALUES 
    ((SELECT user_id FROM user WHERE user_name = 'employee'))
    """)
    
    # Insert sample data into manager table
    cursor.execute("""
    INSERT INTO manager (user_id) VALUES 
    ((SELECT user_id FROM user WHERE user_name = 'manager'))
    """)
    
    # Insert sample data into admin table
    cursor.execute("""
    INSERT INTO admin (user_id) VALUES 
    ((SELECT user_id FROM user WHERE user_name = 'admin'))
    """)
    
    # Insert sample data into project table
    cursor.execute("""
    INSERT INTO project (Project_name, manager_id) VALUES 
    ('Project Alpha', (SELECT manager_id FROM manager m JOIN user u ON m.user_id = u.user_id WHERE u.user_name = 'manager'))
    """)
    
    # Insert sample data into task table
    cursor.execute("""
    INSERT INTO task (task_name, deskripsi, id_employee, project_id) VALUES 
    ('Task 1', 'Description for Task 1', (SELECT employee_id FROM employee e JOIN user u ON e.user_id = u.user_id WHERE u.user_name = 'employee'), (SELECT ProjectID FROM project WHERE Project_name = 'Project Alpha'))
    """)

    db.commit()