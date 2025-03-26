from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT, done BOOLEAN)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return jsonify(message="Hello, Flask!")

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (task['name'], task['done']))
    conn.commit()
    conn.close()
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    res = c.execute("SELECT name, done FROM tasks")
    tasks = res.fetchall()
    conn.close()
    return jsonify(tasks), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
