from database.db import check_user_exists, insert_user, validate_login, hash_password

def sign_up_user(full_name, username, password, confirm_password):
    if password != confirm_password:
        return False, "Passwords do not match."
    if check_user_exists(username):
        return False, "Username already exists."
    insert_user(full_name, username, hash_password(password))
    return True, "Account created successfully."

def login_user(username, password):
    user = validate_login(username, password)
    if user:
        return True, user[1]  # Return full_name
    else:
        return False, "Invalid username or password."
