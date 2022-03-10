import threading
from sqlalchemy import create_engine, Column, Numeric, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from bot import SQL_DB

def start() -> scoped_session:
    engine = create_engine(SQL_DB, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()
INSERTION_LOCK = threading.RLock()

class Users(BASE):
    __tablename__ = "bot"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

Users.__table__.create(checkfirst=True)

def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Users).get(id)
        if not msg:
            usr = Users(id, user_name)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass

def remove_user(id):
    with INSERTION_LOCK:
        msg = SESSION.query(Users).get(id)
        if msg:
            SESSION.delete(msg)
            SESSION.commit()
        else:
            SESSION.close()
      
def count_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()

def user_list():
    try:
        query = SESSION.query(Users.id).order_by(Users.id)
        return query
    finally:
        SESSION.close()
