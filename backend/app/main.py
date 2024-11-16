from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, database
import os
from .database import engine
from .models import Base

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Монтируем директорию для статических файлов
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# Добавляем обработку CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Маршруты для работы с изображениями
@app.get("/images/", response_model=list[schemas.ImageOut])
def get_images(db: Session = Depends(database.get_db)):
    return db.query(models.Image).all()

@app.get("/images/{image_id}", response_model=schemas.ImageOut)
def get_image(image_id: int, db: Session = Depends(database.get_db)):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

