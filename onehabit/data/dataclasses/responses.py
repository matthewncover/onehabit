from dataclasses import dataclass, field
from pydantic import BaseModel, validator

import uuid, datetime as dt

from ..utils import DataUtils
from ..database import OneHabitDatabase as ohdb

class ResponseMetadata(BaseModel):
    criteria_met: bool = None
    nonzero_criteria_met: bool = None

    criteria_notes: str = None
    nonzero_criteria_notes: str = None

@dataclass
class Response:
    user_id: uuid.UUID = field()
    ref_id: uuid.UUID = field() ## habit or observation

    date: dt.datetime = field(default_factory=dt.datetime.now)
    metadata: ResponseMetadata = field(default_factory=dict)
    
    def add_to_db(self):
        data = DataUtils.make_payload(self)
        ohdb.add_response(data)
