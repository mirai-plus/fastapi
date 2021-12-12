from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class HealthCenters(BaseModel):
    id: int
    nome: str
    struttura: str
    indirizzo: str
    telefono: str
    email: str
    sito: str
    lat: float
    lng: float
    descrizione_breve: str
    descrizione: str
    orari: str
    foto: str
    foto_thumb: str
    foto_thumb_2: str
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True
    