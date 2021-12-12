from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)

class HealthCenters(Base):
    __tablename__ = "health_centers"
    id = Column(Integer, primary_key=True, nullable=False)
    nome: Column(String, nullable=False)
    struttura: Column(String, nullable=False)
    indirizzo: Column(String, nullable=False)
    telefono: Column(String, nullable=True)
    email: Column(String, nullable=True)
    sito: Column(String, nullable=True)
    lat: Column(float, nullable=True)
    lng: Column(float, nullable=True)
    descrizione_breve: Column(String, nullable=True)
    descrizione: Column(String, nullable=True)
    orari: Column(String, nullable=True)
    foto: Column(String, nullable=True)
    foto_thumb: Column(String, nullable=True)
    foto_thumb_2: Column(String, nullable=True)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")