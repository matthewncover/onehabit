import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP
from pydantic import BaseModel

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class HabitVersionData(BaseModel):
    pass

class HabitVersion(SA_BASE):
    __tablename__ = "habit_versions"
    __table_args__ = {"schema": "habits"}

    id = sa.Column(BIGINT, primary_key=True)
    habit_id = sa.Column(BIGINT, sa.ForeignKey("users.habits.id"))
    data = sa.Column(JSONBPydantic(HabitVersionData))

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    habit = relationship("Habit", back_populates="habit_versions")

    def __repr__(self):
        return f"<HabitVersion(id={self.id}, habit_id={self.habit_id})>"
