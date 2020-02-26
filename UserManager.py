from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.Database import *
#sql documentation:
#https://pythonspot.com/login-authentication-with-flask
=======
#from lib.Database import *

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()
 
class PatientID(Base):
    __tablename__ = "patient"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ProviderID(Base):
    __tablename__ = "provider"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 

    def __init__(self, username, password):
        self.username = username
        self.password = password 

# create tables
Base.metadata.create_all(engine)

engine = create_engine('sqlite:///tutorial.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

password = "cs1531"

for email in patient_email:
    pat = PatientID(email,password)
    session.add(pat)
    
for e in provider_email:
    pro = ProviderID(e,password)
    session.add(pro)

# commit the record the database
session.commit()
 
session.commit()





          

