def db_init(cursor):
    cursor.execute("CREATE DATABASE companyDB")
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
        employee_id INT PRIMARY KEY,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS manager (
        manager_id INT PRIMARY KEY,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INT PRIMARY KEY,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task (
        taskID INT UNIQUE PRIMARY KEY NOT NULL,
        task_name VARCHAR(50) NOT NULL,
        deskripsi TEXT NULL,
        id_employee INT NOT NULL,
        FOREIGN KEY (id_employee) REFERENCES employee(employee_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        ProjectID INT UNIQUE PRIMARY KEY NOT NULL,
        Project_name VARCHAR(50) NOT NULL,
        manager_id INT NOT NULL,
        FOREIGN KEY (manager_id) REFERENCES manager(manager_id)
    )
    """)