"""hash_creds.py

Generates SHA-256 hashes for the dashboard client login.

Usage:
    python hash_creds.py
    # then type the username and password when prompted

Paste the two output hashes into config/client_credentials.json under
"username_hash" and "password_hash" respectively. Commit and push.
"""
import hashlib, getpass

u = input("Username: ").strip()
p = getpass.getpass("Password: ")

u_hash = hashlib.sha256(u.encode()).hexdigest()
p_hash = hashlib.sha256(p.encode()).hexdigest()

print()
print("Paste these into config/client_credentials.json:")
print()
print(f'  "username_hash": "{u_hash}",')
print(f'  "password_hash": "{p_hash}"')
