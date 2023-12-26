from .api import APIUtils
from ...data.dataclasses.prompts import Prompts

class Coach:

    BASE_PAYLOAD = {
        "max_tokens": 100,      # to generate
        "stream": False,        # several json outputs breaking up response
        "n": 1,                 # n completions per prompt
        "temperature": 1,       # sampling temp
        "top_k": 30,            # select next output token among `top_k` most likley ones
        "top_p": 0.8            # also truncates tokens (0-1)
    }
    
    def __init__(self):
        pass

    def completion_response(self, message):
        payload = {"prompt": message}
        payload.update(self.BASE_PAYLOAD)

        return APIUtils.post_request(method="completions", payload=payload)


    def chat_response(self, message):
        payload = {"messages": [message], "system": Prompts.base}
        payload.update(self.BASE_PAYLOAD)

        return APIUtils.post_request(method="chat", payload=payload)

    
    def discrete_response(self, context:str, response_set:list):
        """respond with one of a discrete set of responses.
            completion, not chat.
        """
        logprobs = {x: self._get_log_probability(context, x)["logprob"] for x in response_set}
        return max(logprobs, key=logprobs.get)

    def _get_log_probability(self, context:str, continuation:str):
        payload = {
            "context": context,
            "continuation": continuation
        }
        return APIUtils.post_request(method="logprob", payload=payload)
    

    def _tokenize(self, text:str):
        payload = {"text": text}
        return APIUtils.post_request(method="tokenize", payload=payload)