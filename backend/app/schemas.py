from pydantic import BaseModel

class ImageBase(BaseModel):
    description: str

class ImageCreate(ImageBase):
    pass

class ImageOut(ImageBase):
    id: int
    filename: str

    class Config:
        orm_mode = True
