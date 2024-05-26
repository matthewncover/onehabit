from onehabit.data import ohdb
from onehabit.data.schemas import *

class DatabaseUtils:
    @staticmethod
    def make_new_dialogue(user_id, dialogue_name, version=None):
        data = {
            "user_id": user_id,
            "name": dialogue_name,
            "version": version,
            "full_text": [],
            "summarized_text": {}
        }

        dialogue_id = ohdb.add(Dialogue(**data))
        return dialogue_id
