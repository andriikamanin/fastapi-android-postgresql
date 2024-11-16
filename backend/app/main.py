from fastapi import FastAPI, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
import os
from uuid import uuid4

app = FastAPI()

# Создание таблиц
models.Base.metadata.create_all(bind=database.engine)

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/", response_model=schemas.ImageOut)
async def upload_image(
    description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db)
):
    # Сохранение файла
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Сохранение данных в БД
    image = models.Image(filename=filename, description=description)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

@app.get("/images/", response_model=list[schemas.ImageOut])
def get_images(db: Session = Depends(database.get_db)):
    return db.query(models.Image).all()
