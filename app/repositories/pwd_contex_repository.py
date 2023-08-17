from passlib.context import CryptContext


class Pwd_context():
    __pwd_context__ = CryptContext(schemes=['bcrypt'], deprecated='auto')