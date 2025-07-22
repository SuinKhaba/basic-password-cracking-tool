import hashlib
import os

def hash_password(password):
    #auto-generate random 16-byte salt
    salt = os.urandom(16)
    salted = salt + password.encode()

    #hash using SHA-256
    hashed = hashlib.sha256(salted).hexdigest()
    salted_hash = salt.hex() + hashed
    return salted_hash


if __name__ == "__main__":
    password = input("Enter password to hash: ")
    result = hash_password(password)
    print(f"Salted SHA-256 Hash:\n{result}")

    #save to file
    with open("../hashes/salted_hashed_password.txt", "w") as f: 
        f.write(f"Password: {password}\nSalted SHA-256 Hash: {result}\n")
    print("[+] Saved to hashed_password.txt")
