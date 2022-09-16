from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine("sqlite:///./sqlite.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, )