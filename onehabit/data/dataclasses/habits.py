from dataclasses import dataclass, field
from pydantic import BaseModel, validator
from typing import Optional

import uuid, datetime as dt

from ..utils import DataUtils
from ..database import OneHabitDatabase as ohdb

class HabitMetadata(BaseModel):
    name: str
    description: Optional[str] = None
    criteria: str
    nonzero_criteria: str
    days_per_week: int
    half_of_day: Optional[int] = None

    ## TODO include as attributes:
    ## responses to introduction like second-order impacts and such.

    @validator("days_per_week")
    def _val_days_per_week(cls, days_per_week):
        return max(min(days_per_week, 7), 0)
    
    @validator("half_of_day")
    def _val_half_of_day(cls, half_of_day):
        if half_of_day not in [1, 2, None]:
            raise ValueError("`half_of_day` must be `1`, `2`, or `None`")
        return half_of_day

@dataclass
class Habit:
    user_id: uuid.UUID = field()
    metadata: HabitMetadata = field(default_factory=dict)

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    version: str = field(default="001")

    created_date: dt.datetime = field(default_factory=dt.datetime.now)
    active: bool = field(default=False)
    archived: bool = field(default=False)

    def add_to_db(self):
        data = DataUtils.make_payload(self)
        ohdb().add_new_habit(data)

    def bump_version(self):
        if not self._version_bump_required():
            return
        ## add to db
        pass
    
    def _version_bump_required(self):
        return False


@dataclass
class HabitSet:
    user_id: uuid.UUID
    habits: list[Habit] = field(default_factory=list)

    def __post_init__(self):
        self.habits = self._get_habit_set()

    def _get_habit_set(self):
        return [Habit(**x) for x in ohdb().get_habits(self.user_id)]