from dataclasses import dataclass, field
from pydantic import BaseModel, validator

import uuid, datetime as dt

from ..utils import DataUtils
from ..database import OneHabitDatabase as ohdb

class ObservationMetadata(BaseModel):
    name: str

@dataclass
class Observation:
    user_id: uuid.UUID = field()
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    created_date: dt.datetime = field(default_factory=dt.datetime.now)
    metadata: ObservationMetadata = field(default_factory=dict)
    archived: bool = field(default=False)
    
    def add_to_db(self):
        data = DataUtils.make_payload(self)
        ohdb.add_observation(data)
