import psycopg2

# Replace with your actual database credentials
db_host = "postgres"
db_port = 5432
db_name = "your_database_name"
db_user = "your_username"
db_password = "your_password"

try:
    # Establish a connection
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute SQL queries
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    print(f"PostgreSQL version: {result[0]}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
