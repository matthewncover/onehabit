
class Message:

    @staticmethod
    def to_openai_format(role:str, content:str) -> dict:
        message = {
            "role": role.replace("coach", "assistant"),
            "content": content
        }
        return message
    
    @staticmethod
    def from_openai_format(message: dict, coach=False) -> tuple:
        if coach:
            return (message["role"].replace("assistant", "coach"), message["content"])
        
        return (message["role"], message["content"])