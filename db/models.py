from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    quotes = relationship("Quote", back_populates="person")

class DiscordMember(Base):
    __tablename__ = "discord_members"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    discord_id = Column(String)
    discord_username = Column(String)
    person_id = Column(Integer, ForeignKey("people.id"))

    person = relationship("Person", back_populates="discord_user")

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    person_id = Column(Integer, ForeignKey("people.id"))

    person = relationship("Person", back_populates="quotes")