from dataclasses import dataclass, field
import uuid, datetime as dt

from .utils import DataUtils
from .database import OneHabitDatabase as ohdb

#region one goal
@dataclass
class Goal:
    goal_id: uuid.UUID = field(default=uuid.uuid4())
    goal_version: str = field(default="001")

    user_id: uuid.UUID
    created_date: dt.datetime = field(default_factory=dt.datetime.now)
    _goal: dict

    active: bool = field(default=False)
    archived: bool = field(default=False)

    @property
    def goal(self):
        return self._goal
    
    @goal.setter
    def goal(self):
        raise NotImplementedError("Goal JSON validation not implemented")
    
    def make_payload(self):
        return {x: getattr(self, x)
                for x in dir(self)
                if not x.startswith("_")}
    
    def add_to_db(self):
        data = DataUtils.make_payload(self)
        ohdb.add_new_goal(data)

    def bump_version(self):
        if not self._version_bump_required():
            return
        ## add to db
        pass
    
    def _version_bump_required(self):
        return False
    
#endregion

@dataclass
class GoalSet:
    user_id: uuid.UUID
    goals: list[Goal] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.goals = self._get_goal_set()

    def _get_goal_set(self):
        return [Goal(**x) for x in ohdb.get_goals(self.user_id)]