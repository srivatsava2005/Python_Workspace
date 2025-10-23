def login_system():
    # Outer function to manage the login process
    
    def validate_credentials(username, password):
        # Inner function to validate username and password
        stored_username = "admin"
        stored_password = "12345"
        return username == stored_username and password == stored_password
    
    print("=== User Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_credentials(username, password):
        print(f"\nWelcome, {username}! You have successfully logged in.")
    else:
        print("\nInvalid username or password. Please try again.")

# Example usage
login_system()
