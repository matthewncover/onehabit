import os, openai
from dotenv import load_dotenv

from onehabit.data import ohdb
from onehabit.data.schemas import User, Dialogue, Prompt

from onehabit.coach.openai.messages import Message
from onehabit.data.schemas.coach.personalities import Personality

load_dotenv()

class OpenAIModel:
    MODEL = "gpt-3.5-turbo"

    def __init__(self):
        client = openai.OpenAI()
        client.api_key = os.getenv("OPENAI_API_KEY")

        self.client = client

    def _respond(self, messages:list, stream:bool=False):
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=messages,
            stream=stream
        )

        return response if stream else response.choices[0].message.content

    def stream_response(self, stream: openai.Stream):
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content


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

        self._set_prompt(dialogue_name)
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

    def _set_prompt(self, dialogue_name):
        filters = [Prompt.dialogue_name == dialogue_name]
        prompt = ohdb.pull(Prompt, *filters)[0]

        prompt_text = (
            prompt.prompt_text
            .replace(Personality.PROMPT_PLACEHOLDER, 
                     self.user.coach_personality.description)
        )

        self.system_message = Message.to_openai_format(role="system", content=prompt_text)


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


class Summarizer(OpenAIModel):
    def __init__(self):
        super().__init__()