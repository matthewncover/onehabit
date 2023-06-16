import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT, DATE, TEXT, TIMESTAMP, JSONB
from pydantic import BaseModel

from onehabit.data.schemas import SA_BASE
from onehabit.data.utils import JSONBPydantic

class DailyTrackerDataModel(BaseModel):
    pass

class DailyTracker(SA_BASE):
    __tablename__ = "daily_tracker"
    __table_args__ = {"schema": "tracker"}

    id = sa.Column(BIGINT, primary_key=True)
    user_id = sa.Column(BIGINT, sa.ForeignKey("users.users.id"))
    track_date = sa.Column(DATE, nullable=False)
    data = sa.Column(JSONBPydantic(DailyTrackerDataModel), default='{}', nullable=False)
    notes = sa.Column(TEXT)

    created_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)
    modified_at = sa.Column(TIMESTAMP, default=sa.sql.func.now(), nullable=False)

    user = relationship("User", back_populates="daily_trackers")
    habit_reflection = relationship("HabitReflection", back_populates="daily_tracker", uselist=False)

    def __repr__(self):
        return f"<DailyTracker(id={self.id}, date={self.track_date})>"