from cryptography.fernet import Fernet
password = input("ENTER IMPERIAL CLEARANCE CODE: ")

if password == "MNNIT2026": 
    print("\n[VERIFIED] Accessing Vault...")
    
    with open("secret.key", "rb") as key_file:
        saved_key = key_file.read()
    
    lock = Fernet(saved_key)
    with open("vault.txt", "rb") as vault_file:
        scrambled_data = vault_file.read()
    decrypted_message = lock.decrypt(scrambled_data)
    
    print("\n--- IDENTITY VERIFIED ---")
    print("Imperial Secret Revealed:", decrypted_message.decode())

else:
    print("\n[!!! ALERT !!!] ACCESS DENIED. INTRUDER DETECTED.")