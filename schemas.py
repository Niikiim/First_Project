from pydantic import BaseModel

class ServicosSchema(BaseModel):
    item: str
    ref: str
    und: str
    preco: float

    class Config:
        from_atributes = True
