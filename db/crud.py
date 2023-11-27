from sqlalchemy.orm import Session

from . import models, schemas

#####################
## PEOPLE
#####################
def get_person(db: Session, id: int):
    return db.query(models.Person).filter(models.Person.id == id).first()

def get_person_by_name(db: Session, name: str):
    return db.query(models.Person).filter(models.Person.name == name).first()

def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(name=person.name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def find_or_create_person_by_name(db: Session, name: str):
    person = get_person_by_name(db, name)
    if person: return person
    return create_person(db, schemas.PersonCreate(name=name))

#####################
## DISCORD MEMBERS
#####################
def get_discord_member(db: Session, id: int):
    return db.query(models.DiscordMember).filter(models.DiscordMember.id == id).first()

def get_discord_member_by_discord_id(db: Session, discord_id: int):
    return db.query(models.DiscordMember).filter(models.DiscordMember.discord_id == discord_id).first()

def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DiscordMember).offset(skip).limit(limit).all()

def create_discord_member(db: Session, member: schemas.DiscordMemberCreate):
    member_person = find_or_create_person_by_name(db, member.name)
    params = {
        'discord_id': member.discord_id,
        'discord_username': member.discord_username,
        'person_id': member_person.id
    }
    db_member = models.DiscordMember(**params)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

#####################
## QUOTES
#####################
def create_quote(db: Session, quote: schemas.QuoteCreate):
    if quote.person_discord_id:
        person = get_discord_member_by_discord_id(db, quote.person_discord_id).person
    if quote.person_name:
        person = find_or_create_person_by_name(quote.person_name)
    quote_person = find_or_create_person_by_name(quote.person_name)
    db_quote = models.Quote(text = quote.text, person_id = quote_person.id)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def create_quote_from_name(db: Session, quote: schemas.QuoteCreate):
    quote_person = find_or_create_person_by_name(quote.person_name)
    db_quote = models.Quote(text = quote.text, person_id = quote_person.id)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def create_quote_from_member(db: Session, quote: schemas.QuoteCreate):
    quote_person = get_discord_member_by_discord_id(db, quote.person_discord_id).person
    db_quote = models.Quote(text = quote.text, person_id = quote_person.id)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def get_quotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quote).offset(skip).limit(limit).all()

def get_last_quote(db: Session):
    return db.query(models.Quote).last