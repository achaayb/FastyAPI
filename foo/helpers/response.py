from pydantic import BaseModel
import json

def Response(data, message='N/A'):
    return {
        "data": data,
        "code": "success",
        "message": message
    }

class ErrorException(Exception):
    def __init__(self, message: str):
        self.message = message

def Error(message = 'N/A'):
    raise ErrorException(message)

def Error_ws(message = 'N/A'):
    return f'{{"code": "error", "message": "{message}"}}'
