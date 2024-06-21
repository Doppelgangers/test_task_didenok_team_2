from cryptography.fernet import Fernet


class EncryptionService:
    def __init__(self, key: str):
        self.cipher_suite = Fernet(key=key)

    def encrypt(self, plain_text: str) -> str:
        return self.cipher_suite.encrypt(plain_text.encode()).decode()

    def decrypt(self, encrypted_text: str) -> str:
        return self.cipher_suite.decrypt(encrypted_text.encode()).decode()
