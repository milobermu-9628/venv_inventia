from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
#load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/INVENTIA"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:fVcJNNcinwSfNeXDDBKrUFPUymdNxfTQ:@trolley.proxy.rlwy.net:56365/railway"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()