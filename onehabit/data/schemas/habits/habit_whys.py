import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, TIMESTAMP, JSONB
from pydantic import BaseModel

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class HabitWhyDataModel(BaseModel):
    pass

class HabitWhy(SA_BASE):
    __tablename__ = "habit_why"
    __table_args__ = {"schema": "habits"}

    id_seq = sa.Sequence("seq_habit_why_id", schema="habits", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    habit_id = sa.Column(BIGINT, sa.ForeignKey("users.habits.id"))
    why_description = sa.Column(TEXT)
    data = sa.Column(JSONBPydantic(HabitWhyDataModel), nullable=False)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    habit = relationship("Habit", back_populates="habit_why", uselist=False)

    def __repr__(self):
        return f"<HabitWhy(id={self.id}, habit_id={self.habit_id})>"