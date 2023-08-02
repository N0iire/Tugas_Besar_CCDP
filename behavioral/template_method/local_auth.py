from auth_template import AuthTemplate

class LocalAuth(AuthTemplate):
    def get_username(self):
        # Code to get username from user input or session data
        return input("Enter username: ")

    def get_password(self):
        # Code to get password from user input (you might want to hide the input for security)
        return input("Enter password: ")

    def _authenticate(self, username, password):
        # Implement the logic to authenticate against local data (e.g., database)
        # For demonstration purposes, we'll assume the username and password are valid.
        # In a real application, you'd check against a database or other data source.
        valid_users = {"user1": "password1", "user2": "password2"}
        if username in valid_users and valid_users[username] == password:
            return True
        return False
