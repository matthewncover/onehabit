from .database import OneHabitDatabase as ohdb

class DataUtils:

    @staticmethod
    def make_payload(obj):
        return {
            x: getattr(obj, x)
            for x in dir(obj)
            if not x.startswith("_")
        }