from local_auth import LocalAuth
from ldap_auth import LDAPAuth

def main():
    print("Choose the authentication method:")
    print("1. Local Authentication")
    print("2. LDAP Authentication")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        auth = LocalAuth()
    elif choice == '2':
        auth = LDAPAuth()
    else:
        print("Invalid choice. Exiting...")
        return

    if auth.authenticate():
        print("Authentication successful!")
    else:
        print("Authentication failed. Please check your credentials.")

if __name__ == "__main__":
    main()
