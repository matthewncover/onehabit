import bcrypt

class EncryptionUtils:

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
    
    @staticmethod
    def check_password(hashed_password, password_input):
        return bcrypt.checkpw(
            password=password_input.encode('utf-8'),
            hashed_password=hashed_password
        )