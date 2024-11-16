from app.database import SessionLocal
from app.models import Image

db = SessionLocal()

# Добавление записи об изображении
image = Image(filename="test_image.jpg", description="Test image from URL")
db.add(image)
db.commit()
db.refresh(image)

print(f"Added image with ID {image.id}")
