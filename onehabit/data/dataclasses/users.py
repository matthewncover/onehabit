from dataclasses import dataclass
import re, uuid

from .database import OneHabitDatabase as ohdb

class ValidationError(Exception):
    pass

@dataclass
class User:
    user_id: uuid.UUID
    _username: str
    _user_email: str
    password_hash: bytes

    def __setattr__(self, name, value):
        if name not in self.__annotations__:
            raise ValidationError(f"Cannot set attribute {name} on User.")
        super().__setattr__(name, value)

    @classmethod
    def from_existing(cls, username:str):
        user_data = ohdb.get_user(username)
        return cls(**user_data)

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
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError(f"Invalid email address: {value}")
        self._user_email = value

    #endregion

    @staticmethod
    def validate_password(password: str):
        if len(password) < 7:
            raise ValidationError("Password must be > 7 characters")
