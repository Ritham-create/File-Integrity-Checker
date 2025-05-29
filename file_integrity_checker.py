import hashlib
import os

def get_file_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

safe_hashes = {
    "example.txt": "6b44264c46605c6ef71efcfc6d0701e32ec2560b5927ab9de50a736863d10893"
}

folder = "."

print("\n[+] Checking files for suspicious changes...\n")

for filename in os.listdir(folder):
    if filename == "file_integrity_checker.py":  # Skip scanning the script itself
        continue
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        current_hash = get_file_hash(path)
        if filename in safe_hashes:
            if current_hash != safe_hashes[filename]:
                print(f"[!] WARNING: {filename} has been modified!")
            else:
                print(f"[OK] {filename} is safe.")
        else:
            print(f"[?] {filename} not in safe list. Review manually.")

  
