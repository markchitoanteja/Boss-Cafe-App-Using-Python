from database.db import check_user_exists, insert_user, validate_login, hash_password, insert_logout_log

def sign_up_user(full_name, email, username, password, confirm_password):
    if password != confirm_password:
        return False, "Passwords do not match."
    if check_user_exists(username):
        return False, "Username already exists."
    
    insert_user(full_name, email, username, hash_password(password))
    return True, "Account created successfully."

def login_user(username, password):
    user = validate_login(username, password)
    if user:
        # user is a tuple, assuming user[0] is id and user[1] is full_name
        return True, (user[0], user[1])  # return user_id and full_name
    else:
        return False, "Invalid username or password."

def logout_user(user_id):
    insert_logout_log(user_id)
