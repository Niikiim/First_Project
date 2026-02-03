from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Servico (base):
    __tablename__ = "Servicos" #Este será o nom e da tabela 

    id = Column (Integer, primary_key=True, index=True)
    cod = Column(String)
    item = Column(String)
    ref = Column(String)
    und = Column(String)
    preco = Column(Float)

