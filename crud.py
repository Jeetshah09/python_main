import mysql.connector

# Step 1: Establish the connection to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='college'  # Connect to the 'college' database
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Step 2: Create a 'student' table
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
)
"""
cursor.execute(create_table_query)
print("Table 'student' created successfully.")

# Step 3: Perform CRUD Operations

# Create (Insert) - Adding a new student
insert_query = "INSERT INTO student (name, age, grade) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ("Punit Kanzariya", 20, "A"))
conn.commit()
print("New student added.")

# Read (Select) - Fetching all students
cursor.execute("SELECT * FROM student")
students = cursor.fetchall()
print("All Students:")
for student in students:
    print(student)

# Update - Modifying an existing student's information
update_query = "UPDATE student SET age = %s, grade = %s WHERE name = %s"
cursor.execute(update_query, (21, "A+", "John Doe"))
conn.commit()
print("Student information updated.")

# Delete - Deleting a student
delete_query = "DELETE FROM student WHERE name = %s"
cursor.execute(delete_query, ("John Doe",))
conn.commit()
print("Student deleted.")

# Step 4: Close the cursor and connection
cursor.close()
conn.close()
