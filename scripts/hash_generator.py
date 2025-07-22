# this script generates hashes for a list of passwords and writes them to a file.
import hashlib

def generate_hashes(passwords, algo="md5"):
    algo = algo.lower()
    hash_func = {
        "md5": hashlib.md5,
        "sha256": hashlib.sha256,
        "sha1": hashlib.sha1,
        "sha512": hashlib.sha512
    }.get(algo)

    if not hash_func:
        print(f"[!] Unsupported hashing algorithm: {algo}")
        return

    with open(f"../hashes/{algo}_hashes.txt", "w", encoding="utf-8") as f:
        for pwd in passwords:
            pwd = pwd.strip()
            hashed = hash_func(pwd.encode()).hexdigest()
            f.write(f"{pwd} -> {algo.upper()}: {hashed}\n")
    
    print(f"[+] Hashes written to {algo}_hashes.txt")

if __name__ == "__main__":
    import sys
    algo = input("Enter hashing algorithm (md5 / sha1 / sha256 / sha512): ").strip().lower()

    try:
        with open("../hashes/passwords.txt", "r", encoding="utf-8") as file: # enter the wordlist file path
            passwords = file.readlines()
        generate_hashes(passwords, algo)
    except FileNotFoundError:
        print("[!] passwords.txt not found.")
