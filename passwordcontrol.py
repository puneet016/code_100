def password_controller(password):
    if len(password) < 8:
        print("Password is too short")
    elif len(password) > 16:
        print("Password is too long")
    else:
        print("Password is valid")
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit")
        return
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter")
        return  
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter")
        return
    if not any(char in "!@#$%^&*()-+" for char in password):
        print("Password must contain at least one special character")
        return
    print("Password is valid")
password = input("Enter your password: ")
password_controller(password)