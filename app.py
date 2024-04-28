from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_task():
    # Extract the title of the task from the form data
    title = request.form['title']
    
    # Connect to the database
    conn = get_db_connection()
    
    # Execute SQL query to insert the task into the 'tasks' table
    conn.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    
    # Commit the transaction
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    # Redirect the user back to the homepage after adding the task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
