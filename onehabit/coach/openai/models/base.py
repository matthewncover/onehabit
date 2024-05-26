import os, openai
from typing import Callable, Optional
from dotenv import load_dotenv

from onehabit.data import ohdb
from onehabit.data.schemas.coach.prompts import Prompt

from onehabit.coach.openai.messages import Message

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

    def _set_prompt(self, dialogue_name:str, dynamic_prompt_fn:Optional[Callable] = lambda x: x):
        filters = [Prompt.dialogue_name == dialogue_name]
        prompt = ohdb.pull(Prompt, *filters)[0]
        prompt_text = dynamic_prompt_fn(prompt.prompt_text)

        self.system_message = Message.to_openai_format(role="system", content=prompt_text)