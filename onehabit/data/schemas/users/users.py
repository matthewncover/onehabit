from typing import Optional, Union

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR, BYTEA, BIGINT
from pydantic import BaseModel, EmailStr, ValidationError, constr, validator, Field

from onehabit.data.encryption import EncryptionUtils
from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class NewUserValidationError(Exception):
    def __init__(self, e: ValidationError):
        self.pydantic_errors = e.errors()
        self.construct_display_msgs()

    def construct_display_msgs(self):
        self.display_msgs = [
            getattr(self, f"_{error['loc'][0]}_msg")(error)
            for error in self.pydantic_errors
        ]
        
    def _username_msg(self, error: dict):
        return error["msg"].replace("String", error["loc"][0])
    
    def _email_msg(self, error: dict):
        reason: str = error["msg"].split("valid.")[-1].lower().strip().strip(".")
        return f"invalid email, {reason}"
    
    def _password_msg(self, error: dict):
        return error["msg"].replace("String", error["loc"][0])

class UserValidationModel(BaseModel):
    username: constr(min_length=5)
    email: Union[EmailStr, None]
    password: constr(min_length=5)

    @validator("username")
    def username_val(cls, v):
        if any(not (x.isalnum() or x in ["-_"]) for x in v):
            raise ValueError("Invalid username")
        return v
        

class UserDataModel(BaseModel):
    pass


class User(SA_BASE):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}
    
    id_seq = sa.Sequence("seq_users_user_id", schema="users", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    username = sa.Column(VARCHAR, nullable=False, unique=True)
    email = sa.Column(VARCHAR, unique=True)
    password_hash = sa.Column(BYTEA, nullable=False)
    data = sa.Column(JSONBPydantic(UserDataModel))

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())

    habits = relationship("Habit", back_populates="user", lazy="joined")
    observations = relationship("Observation", back_populates="user", lazy="joined")
    dialogues = relationship("Dialogue", back_populates="user")
    daily_trackers = relationship("DailyTracker", back_populates="user")

    def __init__(self, **kwargs):
        data = {k: kwargs.get(k) for k in ["username", "email", "password"]}
        
        try:
            valid_data = UserValidationModel(**data)
        except ValidationError as e:
            raise NewUserValidationError(e)
        
        password_hash = EncryptionUtils.hash_password(valid_data.password)
        user_data = {
            "username": valid_data.username,
            "email": valid_data.email,
            "password_hash": password_hash,
            "data": kwargs.get("data")
        }
        
        super().__init__(**user_data)
        
    def __repr__(self):
        return f"<User(username={self.username})>"
