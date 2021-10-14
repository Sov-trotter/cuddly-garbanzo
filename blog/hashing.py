from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def encrypt(password:str):
        return pwd.hash(password)

    def verify(hashed_password:str, entered_password:str):
        return pwd.verify(entered_password, hashed_password)
