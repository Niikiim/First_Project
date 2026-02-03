from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Cria o arquivo do banco na sua pasta
SQLALCHEMY_DATABASE_URL= "sqlite:///./orcamento.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocomit = False, autoflush = False, bind = engine)


#Cria as tabelas de verdade no arquivo.db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()