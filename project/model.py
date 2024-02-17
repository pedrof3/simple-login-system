from sqlalchemy import create_engine, String,Integer, Date, Column
from sqlalchemy.orm import sessionmaker, declarative_base

USER = 'test_user'
PASSWORD = 'user123'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'sistema_cadastro'

CONN = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Users(Base):
    '''
        Responsable to create a table 'Users' in the database with the respectives atributes
    '''
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    birthdate = Column(Date, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

Base.metadata.create_all(engine)
