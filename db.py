import os
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

load_dotenv()


engine = create_engine(os.getenv('DB'))

session = Session(bind=engine)


Base = declarative_base()


class Vacancies(Base):
    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True)
    vacancy_id = Column(String(100))
    vacancy_name = Column(String())
    vacancy_url = Column(String())
    created_at = Column(DateTime(), default=datetime.now())


Base.metadata.create_all(engine)
