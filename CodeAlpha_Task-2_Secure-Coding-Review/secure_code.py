
# Improved and safer login example
import hashlib
import getpass

# Simulated stored user data (would normally come from a database)
STORED_USERNAME = "admin"

# Password "admin123" hashed using SHA-256
STORED_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    """Authenticate user by comparing hashed passwords."""
    if username != STORED_USERNAME:
        return False

    return hash_password(password) == STORED_PASSWORD_HASH


# ---- Program Execution ----
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")  # hides password input

if authenticate(username, password):
    print("Login successful")
else:
    print("Invalid credentials")
