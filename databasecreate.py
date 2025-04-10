import mysql.connector

# Step 1: Establish the connection to MySQL
conn = mysql.connector.connect(
    host='localhost',       # or the host where your MySQL server is running
    user='root',            # your MySQL username
    password=''     # your MySQL password
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Step 2: Create the database 'college'
cursor.execute("CREATE DATABASE IF NOT EXISTS college")

# Step 3: Check if the database exists
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

# Check if 'college' exists in the list of databases
if ('college',) in databases:
    print("The database 'college' has been created successfully.")
else:
    print("Failed to create the database 'college'.")

# Close the cursor and connection
cursor.close()
conn.close()
