# env_manager/src/env_manager/infrastructure/database/connection.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv() # Carrega variáveis do arquivo .env

DB_USER = os.getenv("DB_USER_REMOTE") # Use XXXXXX como placeholder no .env se não quiser commitar
DB_PASSWORD = os.getenv("DB_PASSWORD_REMOTE")
DB_HOST = os.getenv("DB_HOST_REMOTE")
DB_NAME = os.getenv("DB_NAME_REMOTE")

if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise ValueError("Database credentials not found in environment variables.")

# DATABASE_URL = f"mysql+mysqlclient://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

print("Database Remote: ", DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        