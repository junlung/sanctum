from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True


class DiscordMemberBase(BaseModel):
    first_name: str
    last_name: str
    discord_id : str
    discord_username: str


class DiscordMemberCreate(DiscordMemberBase):
    pass

class DiscordMember(DiscordMemberBase):
    id: int

    class Config:
        orm_mode = True


class QuoteBase(BaseModel):
    text: str
    person_id: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int

    class Config:
        orm_mode = True