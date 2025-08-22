# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from database import db  # Import db from database.py
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os
import time

app = Flask(__name__)
CORS(app)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize db with the Flask app

from models import User, Idea  # Import models after db initialization

# Function to check if database is ready
def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
            engine.connect()
            print("Database connection successful!")
            return True
        except OperationalError as e:
            print(f"Database not ready, retrying... ({retries} retries left): {e}")
            retries -= 1
            time.sleep(5)  # Wait 5 seconds before retrying
    return False

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Ideate API"})

if __name__ == '__main__':
    with app.app_context():
        # Wait for the database to be ready
        if wait_for_db():
            try:
                db.create_all()  # Create database tables
                print("Tables created successfully!")
            except Exception as e:
                print(f"Error creating tables: {e}")
        else:
            print("Could not connect to the database. Exiting...")
            exit(1)
    app.run(debug=True, host='0.0.0.0', port=5000)