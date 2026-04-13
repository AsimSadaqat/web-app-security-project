from flask import Flask, render_template, request, jsonify
import sqlite3
import logging
from flask_wtf import CSRFProtect

# Security imports
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import escape
from flask_talisman import Talisman

# Rate Limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# NEW: CORS

from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
csrf = CSRFProtect(app)

# =========================
# LOGGING CONFIGURATION
# =========================
logging.basicConfig(
    filename='security.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started")

# =========================
# SECURITY HEADERS (CSP ENABLED)
# =========================
Talisman(app)

# =========================
# CORS CONFIGURATION
# =========================
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

# =========================
# API KEY (SIMPLE SECURITY)
# =========================
API_KEY = "secret123"

# =========================
# RATE LIMITER
# =========================
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)

# =========================
# LOGIN ATTEMPT TRACKING
# =========================
failed_attempts = {}

# =========================
# DATABASE SETUP
# =========================
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# =========================
# HOME
# =========================
@app.route('/')
def home():
    return render_template('home.html')

# =========================
# REGISTER
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 3:
            logging.warning("Invalid username attempt")
            return "Invalid username (min 3 characters)"

        if len(password) < 6:
            logging.warning(f"Weak password attempt for user: {username}")
            return "Password must be at least 6 characters"

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        hashed_password = generate_password_hash(password)
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))

        conn.commit()
        conn.close()

        logging.info(f"User registered: {username}")

        return "User Registered Securely!"

    return render_template('register.html')

# =========================
# LOGIN (RATE LIMITED)
# =========================
@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in failed_attempts:
            failed_attempts[username] = 0

        if failed_attempts[username] >= 5:
            return "Account temporarily locked due to multiple failed attempts"

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[1], password):
            failed_attempts[username] = 0
            logging.info(f"Successful login: {username}")
            return f"Welcome {username}"
        else:
            failed_attempts[username] += 1
            logging.warning(f"Failed login attempt: {username}")
            return "Login Failed"

    return render_template('login.html')

# =========================
# SEARCH (XSS PROTECTED)
# =========================
@app.route('/search')
def search():
    query = request.args.get('q', '')
    logging.info(f"Search query: {query}")
    return f"You searched for: {escape(query)}"

# =========================
# 🔐 PROTECTED API ENDPOINT
# =========================

@app.route('/api/data')
def api_data():
    api_key = request.headers.get('x-api-key')  

    if api_key != "secret123":
        return {"error": "Unauthorized"}, 401

    return {"message": "Secure API Access Granted"}
# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    print("Server running at: http://127.0.0.1:5000")
    app.run(debug=True)