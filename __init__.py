from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models,schemas,database


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/item/")
async def create_item(servico:schemas.ServicosSchema, db: Session = Depends(database.get_db)):
    #Transforma o dado da web em um dado de Banco
    db_servico = models.ServicoDB(**servico.dict())
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico