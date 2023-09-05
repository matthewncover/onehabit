from dataclasses import dataclass, field
import re, uuid

from ..database import OneHabitDatabase as ohdb
from ..utils import DataUtils

class ValidationError(Exception):
    pass

@dataclass
class User:
    id: uuid.UUID
    _username: str = field(repr=False)
    _email: str = field(repr=False)
    password_hash: bytes

    def __setattr__(self, name, value):
        if name not in self.__annotations__:
            raise ValidationError(f"Cannot set attribute {name} on User.")
        super().__setattr__(name, value)

    @classmethod
    def from_existing(cls, username:str):
        db = ohdb()
        data = ohdb.get_user(db, username)
        return cls(id=data["id"],
                   _username=data["username"],
                   _email=data["email"],
                   password_hash=data["password_hash"])

    #region username
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        if len(value) <= 5 or any(not char.isalnum() for char in value):
            raise ValidationError("Username must be > 5 characters and cannot have whitespace or special characters.")
        self._username = value

    #endregion
    #region email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError(f"Invalid email address: {value}")
        self._email = value

    #endregion

    @staticmethod
    def validate_password(password: str):
        if len(password) < 7:
            raise ValidationError("Password must be > 7 characters")
        
    def add_to_db(self):
        data = DataUtils.make_payload(self)
        db = ohdb()
        ohdb.add_new_user(db, data)
