import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR, BYTEA, BIGINT
from pydantic import BaseModel, EmailStr, ValidationError, constr, validator, Field

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class UserValidationModel(BaseModel):
    username: constr(min_length=5)
    email: EmailStr
    password: constr(min_length=5)

    @validator("username")
    def username_val(cls, v):
        if any(not (x.isalnum() or x in ["-_"]) for x in v):
            raise ValueError("Invalid username")
        

class UserDataModel(BaseModel):
    pass


class User(SA_BASE):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}
    
    id = sa.Column(BIGINT, primary_key=True)
    username = sa.Column(VARCHAR, nullable=False)
    email = sa.Column(VARCHAR)
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
            UserValidationModel(**data)
        except ValidationError:
            raise ValidationError
        
        super().__init__(**kwargs)
        # for k, v in kwargs.items():
        #   setattr(self, k, v)

    def __repr__(self):
        return f"<User(username={self.username})>"
