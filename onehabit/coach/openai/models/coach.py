from onehabit.data import ohdb
from onehabit.data.schemas import User, Dialogue, Prompt

from onehabit.coach.openai.models import OpenAIModel
from onehabit.coach.openai.messages import Message
from onehabit.data.schemas.coach.personalities import Personality

class NoOpenDialogueError(Exception):
    pass

class Coach(OpenAIModel):
    def __init__(self, user: User):
        super().__init__()
        
        self.user = user
        self.user.init_coach_settings()

    #region methods

    def open_dialogue(self, dialogue_name):
        filters = [Dialogue.user_id == self.user.id, Dialogue.name == dialogue_name]
        self.dialogue = ohdb.pull(Dialogue, *filters)[0]

        self._set_prompt(dialogue_name, dynamic_prompt_fn=self._inject_personality)
        return self.dialogue

    def respond(self):
        if not hasattr(self, "system_message"):
            raise NoOpenDialogueError

        messages = self.dialogue.full_text + [self.system_message]
        print(self.system_message["content"])
        response = self._respond(messages)
        self.update_dialogue(role="coach", response=response)

        return response
    
    def update_dialogue(self, role:str, response: str):
        self._verify_turn(next_role=role)

        response_openai_format = Message.to_openai_format(role=role, content=response)
        self.dialogue.full_text.append(response_openai_format)
        ohdb.update(self.dialogue)

    #endregion
    #region helper methods
        
    def _inject_personality(self, prompt_text):
        modified_prompt_text = (
            prompt_text
            .replace(Personality.PROMPT_PLACEHOLDER, 
                     self.user.coach_personality.description)
        )
        return modified_prompt_text

    def _verify_turn(self, next_role: str):
        """ verify the chat being saved is for a role that is not
        the most recent message's role
        """
        if not self.dialogue.full_text:
            return
        
        last_role = self._last_role()
        assert next_role != last_role, f"saving two messages in a row from {next_role}"

    def _last_role(self):
        return self.dialogue.full_text[-1]["role"].replace("assistant", "coach")
    
    def next_role(self):
        last_role = self._last_role()
        return "user" if last_role == "coach" else "coach"
    
    def n_messages(self):
        return len(self.dialogue.full_text)

    #endregion