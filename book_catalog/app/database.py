from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_fc14_user:Dm05fdlZN0I9DP5bqhPLtoSfJIJER3Nu@dpg-cri8p12j1k6c73ar51g0-a.singapore-postgres.render.com/sit722_part3_fc14" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
