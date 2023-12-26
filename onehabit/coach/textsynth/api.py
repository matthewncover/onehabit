import os, requests

from dotenv import load_dotenv
load_dotenv()

class Base:
    
    BASE_URL = "https://api.textsynth.com/v1/engines/"
    MODEL = "llama2_7B"

    url = BASE_URL + MODEL
    token = os.getenv("TEXTSYNTH_API_KEY")
    header = {"Authorization": f"Bearer {token}"}


class APIUtils(Base):

    METHODS = ["completions", "chat"]

    @classmethod
    def post_request(cls, method:str, payload:dict):
        assert method in cls.METHODS

        response = requests.post(url=cls.url+f'/{method}',
                             headers=cls.header,
                             json=payload)
        
        return response.json()
    
    @classmethod
    def credits_remaining(cls):
        url="https://api.textsynth.com/v1/credits"
        response = requests.get(url=url, headers=cls.header)
        return response.json()["credits"]