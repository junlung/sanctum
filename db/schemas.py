from pydantic import BaseModel

#####################
## PEOPLE
#####################
class PersonBase(BaseModel):
    name: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True

#####################
## DISCORD MEMBERS
#####################
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

#####################
## QUOTES
#####################
class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    person_name: str

class Quote(QuoteBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True