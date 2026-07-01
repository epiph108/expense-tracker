from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABSE_URL = "sqlite:///./expenses.db"

engine = create_engine(DATABSE_URL, connect_args = {"check_same_thread" : False})
SessionLocal = sessionmaker(bind=engine, autocommit = False, autoflush = False)

class Base(DeclarativeBase):
  pass

def get_db():
  db = SessionLocal()
  try:
    yield db 
  finally:
    db.close()
  