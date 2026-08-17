"""Simple login function for the Personal Task Tracker."""

import hashlib


def hash_password(password):
    """Return the SHA-256 hash of a password."""
    return hashlib.sha256(password.encode()).hexdigest()


# Registered users, stored as username -> hashed password.
USERS = {
    "tharun": hash_password("task123"),
    "guest": hash_password("guest123"),
}


def login(username, password):
    """Check a username and password.

    Returns True if the credentials match a registered user, otherwise False.
    """
    if username not in USERS:
        return False
    return USERS[username] == hash_password(password)


if __name__ == "__main__":
    print("Login demo")
    print("tharun / task123  ->", login("tharun", "task123"))
    print("tharun / wrongpw  ->", login("tharun", "wrongpw"))
    print("nobody / task123  ->", login("nobody", "task123"))
