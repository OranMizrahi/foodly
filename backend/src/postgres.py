import psycopg2

db_port = 5433
db_name = "mydb"
db_user = "oran"
db_password = "123123"

try:
    # Establish a connection
    conn = psycopg2.connect(
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
    print(f"PostgreSQL version: {result}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
