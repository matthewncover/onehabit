import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, TEXT, TIMESTAMP

from onehabit.data.schemas import SA_BASE

class HabitReflection(SA_BASE):
    __tablename__ = "habit_reflections"
    __table_args__ = {"schema": "tracker"}

    id_seq = sa.Sequence("seq_habit_reflections_id", schema="tracker", metadata=SA_BASE.metadata)
    id = sa.Column(BIGINT, id_seq, server_default=id_seq.next_value(), primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    habit_id = sa.Column(BIGINT, sa.ForeignKey("users.habits.id"))
    daily_tracker_id = sa.Column(BIGINT, sa.ForeignKey("tracker.daily_tracker.id"))
    reflection = sa.Column(TEXT)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    habit = relationship("Habit", back_populates="habit_reflections")
    daily_tracker = relationship("DailyTracker", back_populates="habit_reflection", uselist=False)

    def __repr__(self):
        return f"<HabitReflection(id={self.id}, habit_id={self.habit_id})>"