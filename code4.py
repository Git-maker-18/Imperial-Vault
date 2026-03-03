import os
from cryptography.fernet import Fernet

if os.path.exists("secret.key"):
    with open("secret.key", "rb") as key_file:
        my_key = key_file.read()
    print("[INFO] Using existing key found in 'secret.key'")
else:
    my_key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(my_key)
    print("[INFO] New key generated and secured.")

lock = Fernet(my_key)
my_secret = "The rebel spies are at the north gate".encode()
scrambled_message = lock.encrypt(my_secret)

print("\nA spy would only see this gibberish:")
print(scrambled_message)
with open("vault.txt", "wb") as vault_file:
    vault_file.write(scrambled_message)

print("\n[SUCCESS] The secret has been locked in 'vault.txt'!")