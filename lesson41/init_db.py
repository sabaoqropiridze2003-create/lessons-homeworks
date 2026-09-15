from database import engine
from models import Base

def init_database():
    print("creating tables in database")
    Base.metadata.create_all(bind=engine)
    print("tables were created sucsesfuly")
