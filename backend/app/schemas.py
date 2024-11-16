from pydantic import BaseModel

class ImageBase(BaseModel):
    description: str

class ImageOut(ImageBase):
    id: int
    filename: str

    class Config:
        orm_mode = True
