from dataclasses import dataclass, field
import uuid
import datetime as dt

from .utils import DataUtils
from .database import OneHabitDatabase as ohdb

@dataclass
class Response:
    response_id: uuid.UUID = field(default_factory=uuid.uuid4)
    user_id: uuid.UUID
    
    response_date: dt.datetime = field(default_factory=dt.datetime.now)
    _response: dict

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value: dict):
        # Placeholder for any validation logic for the response JSON
        # if some_condition: 
        #     raise ValidationError("Invalid response JSON.")
        self._response = value

    def make_payload(self):
        return {
            x: getattr(self, x)
            for x in dir(self)
            if not x.startswith("_")
        }

    def add_to_db(self):
        data = DataUtils.make_payload(self)
        ohdb.add_response(data)
