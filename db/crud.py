from sqlalchemy.orm import Session

from . import models, schemas

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

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


def get_discord_member(db: Session, discord_member_id: int):
    return db.query(models.DiscordMember).filter(models.DiscordMember.id == discord_member_id).first()

def get_discord_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DiscordMember).offset(skip).limit(limit).all()

def create_discord_member(db: Session, discord_member: schemas.DiscordMemberCreate):
    db_member = models.DiscordMember(**discord_member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_last_quote(db: Session):
    return db.query(models.Quote).last