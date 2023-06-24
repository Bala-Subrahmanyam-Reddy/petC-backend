from datetime import datetime
from pydantic import BaseModel


class user(BaseModel):
    id: str
    name: str
    email: str
    password: str
    is_verified: bool
    pet_age: str
    pet_bread: str


class userInput(BaseModel):
    name: str
    email: str
    password: str
    pet_age: str
    pet_bread: str


class userUpdateInput(BaseModel):
    name: str
