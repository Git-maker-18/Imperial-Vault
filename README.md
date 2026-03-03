# Imperial-Vault
Project Description: "The Imperial Aegis" – Secure Vault & Identity Verification System

Overview: Developed a two-tier digital fortress designed to protect sensitive Imperial secrets through advanced cryptographic protocols. The system ensures data privacy by rendering information unreadable to unauthorized entities and requires multi-factor authentication for access.

Key Features:

    AES-Standard Encryption: Utilizes the Fernet symmetric encryption algorithm to scramble plaintext data into secure ciphertext, preventing unauthorized data exposure.

    Decoupled Key Management: Implements a security best practice by storing the master decryption key separately from the encrypted data vault.

    Two-Factor Identity Verification: Requires both a physical "Master Key" file and a secret "Clearance Code" (password) to grant access, mitigating the risk of stolen credentials.

    Anomaly Defense: Built-in logic to detect unauthorized access attempts and immediately terminate the decryption process if credentials fail.
    Tools Used: Python 3.11, Cryptography library (Fernet), File I/O for secure storage.
