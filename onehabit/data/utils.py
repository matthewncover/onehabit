import json
from uuid import UUID
from dataclasses import is_dataclass, fields

from pydantic import BaseModel
from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import JSONB

class JSONBPydantic(TypeDecorator):
    impl = JSONB

    def __init__(self, model: BaseModel):
        self.model = model
        super().__init__()

    def process_bind_param(self, value, dialect):
        if value is not None:
                return value.model_dump_json()
        return value
    
    def process_result_value(self, value, dialect):
        if value is not None:
            if isinstance(value, str):
                value = json.loads(value)
            return self.model(**value)
        return value        


class DataUtils:

    @staticmethod
    def make_payload(obj):
        if is_dataclass(obj):
            return {f.name: DataUtils._prepare_value(getattr(obj, f.name))
                    for f in fields(obj)}
        elif isinstance(obj, BaseModel):
            return {k: DataUtils._prepare_value(v)
                    for k, v in obj.model_dump().items()}
        else:
            raise ValueError("Unsupported object type.")

    @staticmethod
    def _prepare_value(value):
        if isinstance(value, UUID):
            return str(value)
        
        if isinstance(value, BaseModel):
            return value.model_dump_json()
        
        if is_dataclass(value):
            return DataUtils.make_payload(value)
        
        return value
