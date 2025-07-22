#password cracking script
#this script attempts to crack a given hash using a wordlist.
import hashlib
import os

def identify_hash_type(hash_value):
    length = len(hash_value)
    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    elif length == 128:
        return "sha512"
    else:
        return None

def get_hash_function(hash_type):
    return {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }.get(hash_type)

def crack_hash(hash_value, wordlist_path):
    hash_type = identify_hash_type(hash_value)
    if not hash_type:
        print("Unable to determine hash type.")
        return

    hash_func = get_hash_function(hash_type)
    if not hash_func:
        print(f"Unsupported hash type: {hash_type}")
        return

    print(f"Detected Hash Type: {hash_type.upper()}")

    try:
        with open(wordlist_path, 'r', encoding="utf-8") as f:
            for word in f:
                word = word.strip()
                generated_hash = hash_func(word.encode()).hexdigest()
                if generated_hash == hash_value:
                    print(f"Match found: {word}")
                    return
        print("No match found in the wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    target_hash = input("Enter the hash value: ").strip().lower()
    wordlist_path = input("Enter wordlist file path (e.g., ../hashes/passwords.txt): ").strip()
    crack_hash(target_hash, wordlist_path)
