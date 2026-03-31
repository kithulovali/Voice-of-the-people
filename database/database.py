from sqlalchemy.orm import sessionmaker , DeclarativeBase 
from sqlalchemy import create_engine 
import os 
from dotenv import load_dotenv  


load_dotenv() 

DATABASE_URL = os.get_env("DATABASE_URL")

engine = create_engine(
    DATABASE_URL, echo = True , 
) 

session_local =sessionmaker(
    bind=engine ,utoflush =False ,autoommit =False
) 

class Model(DeclarativeBase):
   pass 

def get_connection():
    db  = session_local()
    try :
        yield db
    finally :
     db
    