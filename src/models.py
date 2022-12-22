from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: str
    access_key : str