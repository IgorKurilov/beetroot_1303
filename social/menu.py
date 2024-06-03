from post import Post
import bcrypt
import sqlite3
import re

def display_menu():
    print("1. Login")
    print("2. Register")
    print("3. Add post")
    print("4. See all posts")
    print("5. Like post")
    print("6. Dislike post")
    print("0. Exit")
    choice = input("Select an option: ")
    return choice

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""

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

if __name__ == "__main__":
    while True:
        print("Welcome to the new social")
        choice = display_menu()
        match choice:
            case "1":
                # Placeholder for login functionality
                print("Login functionality is not implemented yet.")
            case "2":
                register()
            case "3":
                Post()
            case "4":
                Post.show_posts()
            case "5":
                Post.like()
            case "6":
                Post.dislike()
            case "0":
                break
            case _:
                print("Wrong choice")
