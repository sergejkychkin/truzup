from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,create_engine
from sqlalchemy.orm import sessionmaker
import datetime
engine = create_engine('sqlite:///sql.db', echo=True)
Base = declarative_base()
Session = sessionmaker(engine)





class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    text = Column(String(128))
    date = Column(DateTime,default=datetime.datetime.utcnow)





if __name__ == '__main__':
    Base.metadata.create_all(engine)
