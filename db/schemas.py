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
    discord_id : int
    discord_username: str

class DiscordMemberCreate(DiscordMemberBase):
    name: str

class DiscordMember(DiscordMemberBase):
    id: int
    person_id: int
    
    class Config:
        orm_mode = True

#####################
## QUOTES
#####################
class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    person_name : str = None
    person_discord_id : int = None

class Quote(QuoteBase):
    id: int
    person_id: int

    class Config:
        orm_mode = True