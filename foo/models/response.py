from pydantic import BaseModel

class RES_base():
    code: str
    message: str
    
    def __init__(Sub):
        self.data = Sub