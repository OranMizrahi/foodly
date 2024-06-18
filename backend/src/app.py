from flask import Flask, render_template, request, redirect, url_for
import uuid
import psycopg2
from postgres import Postgress  # Assuming you have a separate file for Postgress class

app = Flask(__name__)

# Initialize PostgreSQL connection
postgres = Postgress()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Generate unique user ID
        user_id = str(uuid.uuid4())

        # Prepare user data dictionary
        user_data = {
            "UserID": user_id,
            "FirstName": first_name,
            "LastName": last_name,
            "Email": email,
            "UserName": username,
            "Password": password
        }

        # Connect to PostgreSQL
        postgres.connect()

        # Execute INSERT query
        postgres.execute(user_data)

        # Close PostgreSQL connection
        postgres.close()

        return redirect(url_for('success'))
    
    return render_template('index.html')
@app.route('/success')
def success():
    return 'User data successfully stored in PostgreSQL!'

@app.route('/search', methods=['GET'])
def search():
    search_name = request.args.get('search_name')
    postgres.connect()
    postgres.cursor.execute("SELECT * FROM foodly_user WHERE FirstName = %s OR LastName = %s", (search_name, search_name))
    search_results = postgres.cursor.fetchall()
    postgres.close()
    return render_template('search_results.html', results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
