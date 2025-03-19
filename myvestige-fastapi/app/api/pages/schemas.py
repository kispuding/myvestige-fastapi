from pydantic import BaseModel


class PageBase(BaseModel):
    title: str
    content: str
    hash: str

class PageCreate(PageBase):
    pass

class PageOut(PageBase):
    id: int

    class Config:
        orm_mode = True