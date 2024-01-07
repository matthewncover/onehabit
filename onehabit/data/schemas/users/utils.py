from onehabit.data import ohdb
from onehabit.data.schemas.coach import Personality

class UserUtils:

    @staticmethod
    def init_coach_settings(user):
        personality_id = user.data.coach_personality_id
        coach_personality = ohdb.pull(Personality, Personality.id == personality_id)[0]
        return coach_personality