from onehabit.data.schemas import User
from onehabit.coach.openai.models import OpenAIModel

class Moderator(OpenAIModel):
    def __init__(self, user: User):
        super().__init__()

        self.user = user
        self._set_prompt(dialogue_name="moderation.fuckery")

    def intercept_fuckery(self, messages:list):
        response = self._respond(messages)