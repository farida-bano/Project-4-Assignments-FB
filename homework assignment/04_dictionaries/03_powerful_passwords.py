
from hashlib import sha256
#hashlib: This is a built-in Python module that provides various cryptographic hashing algorithms, such as SHA-1, SHA-256, MD5, etc.
#sha256: This is a specific function within the hashlib module that implements the SHA-256 (Secure Hash Algorithm 256-bit) hashing algorithm.
def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

# There is no need to edit code beyond this point

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()

    #Example Explanation:
#Here’s what happens in the main() function step by step:
#Testing email example@gmail.com with password word:
#The stored hash for "example@gmail.com" corresponds to the password "password".
#The password "word" is hashed, and the resulting hash doesn't match the stored hash, so login() returns False.
#Testing email example@gmail.com with password password:
#The password "password" matches the stored hash for "example@gmail.com", so login() returns True.
#Testing email code_in_placer@cip.org with password Karel:
#The password "Karel" doesn't match the stored hash for this email ("karel" is the correct password), so the function returns False.
#Testing email code_in_placer@cip.org with password karel:
#The password "karel" matches the stored hash for this email, so login() returns True.
#Testing email student@stanford.edu with password password:
#The stored hash for this email corresponds to the password "123!456?789", so the password "password" doesn’t match the stored hash, and login() returns False.
#Testing email student@stanford.edu with password 123!456?789:
#The password "123!456?789" matches the stored hash for this email, so login() returns True.

