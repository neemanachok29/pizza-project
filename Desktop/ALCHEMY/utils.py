from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def create_database(db_uri):
    db_uri = "sqlite:///database.py"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
