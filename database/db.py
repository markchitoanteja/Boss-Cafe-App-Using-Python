import mysql.connector
import hashlib
from datetime import datetime

# Database configuration
DB_CONFIG = {
    'host': '192.168.1.141',
    'user': 'user_bsit3b',
    'password': 'admin123',
    'database': 'bsit3b'
}

# Hash password with SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Insert a new user
def insert_user(fullname, email, username, password):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO useraccount (fullname, email, username, password)
            VALUES (%s, %s, %s, %s)
        """, (fullname, email, username, password))
        conn.commit()
    except mysql.connector.IntegrityError as e:
        print("Error inserting user:", e)
    finally:
        cursor.close()
        conn.close()

# Check if a user exists
def check_user_exists(username):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM useraccount WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Validate login and log attempt
def validate_login(username, password):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    hashed_pw = hash_password(password)
    cursor.execute("""
        SELECT * FROM useraccount
        WHERE username = %s AND password = %s
    """, (username, hashed_pw))
    user = cursor.fetchone()

    status = "Success" if user else "Failed"

    # Try to get the user ID regardless of success
    userid = None
    if user:
        userid = user[0]  # id is the first field
    else:
        cursor.execute("SELECT id FROM useraccount WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            userid = result[0]

    if userid:
        cursor.execute("""
            INSERT INTO logs (userid, datetime, status)
            VALUES (%s, %s, %s)
        """, (userid, datetime.now(), status))
        conn.commit()

    cursor.close()
    conn.close()
    return user

def insert_logout_log(user_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (userid, datetime, status)
        VALUES (%s, %s, %s)
    """, (user_id, datetime.now(), "Logout"))
    conn.commit()
    cursor.close()
    conn.close()