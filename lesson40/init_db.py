from database import Base, engine
import models

def init_database():
    print("creating tables in database")
    Base.metadata.create_all(bind=engine)
    print("tables were created sucsesfuly")

if __name__ == "__main__":
    init_database()