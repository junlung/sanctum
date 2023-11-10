from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#####################
## PEOPLE
#####################
@app.post("/people/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, name=person.name)
    if db_person:
        raise HTTPException(status_code=400, detail="Person already exists")
    return crud.create_person(db=db, person=person)

@app.get("/people/", response_model=list[schemas.Person])
def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    people = crud.get_people(db, skip=skip, limit=limit)
    return people

@app.get("/people/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@app.get("/people/{person_name}", response_model=schemas.Person)
def read_person(person_name: str, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, person_name)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

#####################
## QUOTES
#####################
@app.post("/quote/", response_model=schemas.Quote)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, quote=quote)