#pip install mysql-connector-python


from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="task_manager_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('add_task.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    category = request.form['category']
    
    cursor.execute("INSERT INTO tasks (name, category) VALUES (%s, %s)", (task_name, category))
    db.commit()
    
    return "Task added successfully!"

@app.route('/another_form')
def show_another_form():
    return render_template('another_form.html')

@app.route('/process_another_form', methods=['POST'])
def process_another_form():
    field1 = request.form['field1']
    field2 = request.form['field2']
    
    # Perform any desired operations with field1 and field2
    
    return "Form submitted successfully!"

@app.route('/yet_another_form')
def show_yet_another_form():
    return render_template('yet_another_form.html')

@app.route('/process_yet_another_form', methods=['POST'])
def process_yet_another_form():
    field3 = request.form['field3']
    field4 = request.form['field4']
    
    # Perform any desired operations with field3 and field4
    
    return "Form submitted successfully!"

@app.route('/report_page')
def report_page():
    return render_template('report_page.html')

@app.route('/api/tasks')
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    tasks_data = [{'id': task[0], 'name': task[1], 'category': task[2], 'status': task[3]} for task in tasks]
    return jsonify(tasks_data)

if __name__ == '__main__':
    app.run(debug=True)
