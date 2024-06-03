import bcrypt
import sqlite3
from validation import is_valid_password

def register():
    login = input("Enter a unique login: ")
    while True:
        password = input("Enter a password: ")
        password_confirmation = input("Confirm your password: ")
        
        if password != password_confirmation:
            print("Passwords do not match. Please try again.")
            continue
        
        is_valid, message = is_valid_password(password)
        if not is_valid:
            print(message)
            continue
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        if save_user(login, hashed_password):
            print("Registration successful!")
            break
        else:
            print("Login already exists. Please choose another one.")

def save_user(login, hashed_password):
    conn = sqlite3.connect('social.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
