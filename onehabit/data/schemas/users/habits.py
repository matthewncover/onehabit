from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP, BOOLEAN
from pydantic import BaseModel, validator, Field

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class HabitDetails(BaseModel):
    name: str = Field(...)
    description: Optional[str] = None
    criteria: str = None
    nonzero_criteria: str = None
    frequency: dict = None
    half_of_day: Optional[int] = None

    @validator("half_of_day")
    def _val_half_of_day(cls, half_of_day):
        if half_of_day not in [1, 2, None]:
            raise ValueError("`half_of_day` must be `1`, `2`, or `None`")
        return half_of_day

class Habit(SA_BASE):
    __tablename__ = "habits"
    __table_args__ = {'schema': "users"}

    id_seq = sa.Sequence("seq_habits_id", schema="users", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    data = sa.Column(JSONBPydantic(HabitDetails))

    active = sa.Column(BOOLEAN, default=True, nullable=False)
    archived = sa.Column(BOOLEAN, default=False, nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now())

    user = relationship("User", back_populates="habits")
    habit_versions = relationship("HabitVersion", back_populates="habit")
    habit_why = relationship("HabitWhy", back_populates="habit", uselist=False)
    habit_reflections = relationship("HabitReflection", back_populates="habit")

    def __repr__(self):
        habit_name = self.data.name
        return f"<Habit(name={habit_name}, user={self.user_id})>"