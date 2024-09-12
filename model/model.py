from pydantic import BaseModel


class Mob(BaseModel):
    battery: int
    weight: int
    sale: int
    