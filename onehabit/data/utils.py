from dataclasses import is_dataclass, fields
from pydantic import BaseModel
from uuid import UUID

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
