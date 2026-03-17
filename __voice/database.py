# package imports 

import os 
from dotenv import load_dotenv 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker  ,DeclarativeBase

load_dotenv() 

class Model(DeclarativeBase):
    pass

#DATABASE setting and configaration 

DATABASE_URL = os.getenv("DATABASE_URL") 

engine = create_engine(DATABASE_URL, echo=True) 

session_local = sessionmaker(bind=engine)

