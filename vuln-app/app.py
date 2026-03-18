from flask import Flask, render_template, request
import sqlite3
import logging

# ✅ Security imports
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import escape
from flask_talisman import Talisman

app = Flask(__name__)

# =========================
# 🧾 LOGGING CONFIGURATION
# =========================
logging.basicConfig(
    filename='security.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started")

# =========================
# 🛡️ SECURITY HEADERS
# =========================
Talisman(app)

# =========================
# 📦 DATABASE SETUP
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
# 🏠 HOME
# =========================
@app.route('/')
def home():
    return "Welcome to Secure App 🛡️"

# =========================
# 🔐 REGISTER (SECURED)
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ✅ Validation
        if len(username) < 3:
            logging.warning("Invalid username attempt")
            return "Invalid username (min 3 characters)"

        if len(password) < 6:
            logging.warning(f"Weak password attempt for user: {username}")
            return "Password must be at least 6 characters"

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # ❌ OLD VULNERABLE CODE
        # c.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")

        # ✅ SECURE VERSION
        hashed_password = generate_password_hash(password)
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))

        conn.commit()
        conn.close()

        logging.info(f"User registered: {username}")

        return "User Registered Securely!"

    return render_template('register.html')

# =========================
# 🔐 LOGIN (SECURED)
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # ❌ OLD VULNERABLE CODE
        # query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        # result = c.execute(query).fetchone()

        # ✅ SECURE VERSION
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[1], password):
            logging.info(f"Successful login: {username}")
            return f"Welcome {username}"
        else:
            logging.warning(f"Failed login attempt: {username}")
            return "Login Failed"

    return render_template('login.html')

# =========================
# 🔐 XSS FIXED
# =========================
@app.route('/search')
def search():
    query = request.args.get('q', '')

    logging.info(f"Search query: {query}")

    # ❌ OLD VULNERABLE CODE
    # return f"You searched for: {query}"

    # ✅ SECURE VERSION
    return f"You searched for: {escape(query)}"

# =========================
# 🚀 RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True)