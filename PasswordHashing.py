import os
import hashlib

def hashPassword(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    return key+salt

def checkPassword(passed_password,actual_password):
    salt = actual_password[32:]
    key = actual_password[:32]
    passed_password_hashing = hashlib.pbkdf2_hmac('sha256',passed_password.encode('utf-8'),salt,100000)
    if passed_password_hashing == key:
        return True
    return False    


