from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

# Инициализируем FastAPI приложение
app = FastAPI()

# Функция для получения базы данных
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания нового элемента
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)
