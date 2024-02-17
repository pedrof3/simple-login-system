import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Users
import argon2

def new_sesion():
    '''
        Lead with database connection
    '''
    USUARIO = 'test_user'
    SENHA = 'user123'
    HOST = 'localhost'
    BANCO = 'sistema_cadastro'
    PORT = '5432'

    CONN = f'postgresql+psycopg2://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def input_verify(cls, name, last_name, birthdate, email, password):
        if len(name) > 50 or len(name) < 3: # Validate name input
            return 2
        if len(last_name) > 50 or len(last_name) < 3: # Validate last_name input
            return 3
        if re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$', birthdate) == False: # Validate birthdate input
             return 4
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email) == False: # Validate email input
            return 5
        if len(password) < 8: # Validate password length
             return 6
        return 1

    @classmethod
    def register(cls, name, last_name, birthdate, email, password):
            session = new_sesion()
            email_verification = session.query(Users).filter(Users.email == email).all()

            if len(email_verification) > 0:
                 return 7
            verified_inputs = cls.input_verify(name, last_name, birthdate, email, password)

            if verified_inputs != 1:
                 return verified_inputs
            try:
                p_hasher = argon2.PasswordHasher()
                hashed_password = p_hasher.hash(password)
                new_user = Users(name=name, last_name=last_name, birthdate=birthdate, email=email, password=hashed_password)
                session.add(new_user)
                session.commit()
                return 1
            except:
                return 8

class ControllerLogin():
    '''
        Responsable to lead with login attempts and manipulation of possible errors
    '''
    @classmethod
    def login_attempt(cls, email_attempt, password_attempt):
        session = new_sesion()
        email_verification = session.query(Users).filter(Users.email == email_attempt).all()

        if len(email_verification) == 0:
            return 2
         
        try:
            ph = argon2.PasswordHasher()
            user_register = session.query(Users).filter(Users.email == email_attempt)
            user_password = user_register[0].password
            ph.verify(user_password, password_attempt)
            return 1
        except:
            return 3
