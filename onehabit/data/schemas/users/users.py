from typing import Optional, Union

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR, BYTEA, BIGINT
from pydantic import BaseModel, EmailStr, ValidationError, conint, constr, validator, Field

from onehabit.data.encryption import EncryptionUtils
from onehabit.data.schemas.base import SA_BASE
from onehabit.data.utils import JSONBPydantic, DataUtils
from onehabit.data.schemas.users.utils import UserUtils

class NewUserValidationError(Exception):

    FIELDS = ["username", "email", "password", "age"]

    def __init__(self, e: ValidationError):
        self.pydantic_errors = e.errors()
        self.construct_display_msgs()

    def construct_display_msgs(self):
        self.display_msgs = [
            getattr(self, f"_{error['loc'][0]}_msg")(error).lower()
            for error in self.pydantic_errors
        ]
        
    def _username_msg(self, error: dict):
        return error["msg"].replace("String", error["loc"][0])
    
    def _email_msg(self, error: dict):
        reason: str = error["msg"].split("valid.")[-1].strip().strip(".")
        return f"invalid email, {reason}"
    
    def _password_msg(self, error: dict):
        return error["msg"].replace("String", error["loc"][0])
    
    def _age_msg(self, error: dict):
        return error["msg"].replace("Input", error["loc"][0])


class UserValidationModel(BaseModel):
    username: constr(min_length=5)
    email: Union[EmailStr, None]
    password: constr(min_length=5)
    age: conint(gt=12, lt=100)

    @validator("username")
    def username_val(cls, v):
        if any(not (x.isalnum() or x in ["-_"]) for x in v):
            raise ValueError("Invalid username")
        return v
        

class UserDataModel(BaseModel):
    age: Optional[int] = None
    setup_complete: Optional[bool] = False
    current_page: Optional[str] = None
    coach_personality_id: Optional[int] = None


class User(SA_BASE):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}
    
    id_seq = sa.Sequence("seq_users_id", schema="users", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    username = sa.Column(VARCHAR, nullable=False, unique=True)
    email = sa.Column(VARCHAR, unique=True)
    password_hash = sa.Column(BYTEA, nullable=False)
    data = sa.Column(JSONBPydantic(UserDataModel), default=UserDataModel())

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())

    habits = relationship("Habit", back_populates="user", lazy="joined")
    observations = relationship("Observation", back_populates="user", lazy="joined")
    dialogues = relationship("Dialogue", back_populates="user")
    daily_trackers = relationship("DailyTracker", back_populates="user")

    def __init__(self, **kwargs):
        data = {k: kwargs.get(k) for k in NewUserValidationError.FIELDS}
        
        try:
            valid_data = UserValidationModel(**data)
        except ValidationError as e:
            raise NewUserValidationError(e)
        
        password_hash = EncryptionUtils.hash_password(valid_data.password)
        user_metadata = UserDataModel() if not kwargs.get("data") else UserDataModel(**kwargs.get("data"))
        user_metadata.age = valid_data.age
        user_data = {
            "username": valid_data.username,
            "email": valid_data.email,
            "password_hash": password_hash,
            "data": user_metadata
        }
        
        super().__init__(**user_data)

    def init_coach_settings(self):
        self.coach_personality = UserUtils.init_coach_settings(self)

    def to_dict(self):
        return DataUtils.serialize(self)

    def __repr__(self):
        return f"<User(username={self.username})>"
