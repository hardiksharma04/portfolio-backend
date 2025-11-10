from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from db_config import get_connection
import os
from waitress import serve

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Portfolio Backend Running ✅"})

@app.route('/add_project', methods=['POST'])
def add_project():
    data = request.get_json()
    title = data['title']
    description = data['description']
    link = data['link']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (title, description, link) VALUES (%s, %s, %s)",
        (title, description, link)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Project Added ✅"})

@app.route('/projects', methods=['GET'])
def get_projects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return jsonify(projects)

if __name__ == "__main__":
    # Use PORT provided by Render, default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so Render can access it externally
    serve(app, host="0.0.0.0", port=port)
