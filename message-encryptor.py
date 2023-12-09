from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a message using the key
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted message using the key
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Generate a key
    key = generate_key()

    # Your message to encrypt
    message_to_encrypt = input("Enter the message to be encoded: ")

    # Encrypt the message
    encrypted = encrypt_message(message_to_encrypt, key)
    print("Encrypted message:", encrypted)

    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print("Decrypted message:", decrypted)
