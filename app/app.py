from flask import Flask, jsonify
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Environment variables
APP_ENV = os.getenv("APP_ENV", "dev")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    message = f"Bu kayıt {APP_ENV.upper()} ortamından geldi"
    created_at = datetime.now()

    cursor.execute(
        "INSERT INTO records (text, created_at) VALUES (%s, %s)",
        (message, created_at)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "status": "OK",
        "environment": APP_ENV,
        "message": message
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "environment": APP_ENV
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)