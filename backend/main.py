from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    rows = res.fetchall()
    conn.close()
    tasks = [{'name': row[0], 'done': row[1]} for row in rows]
    return jsonify(tasks), 201

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
