from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
import datetime

BASE = declarative_base()

def get_timestamp():
    return datetime.datetime.now()
class Todo(BASE):
    __tablename__ = 'to_do'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)
    timestamp = Column(DateTime, default=get_timestamp())

    def __init__(self, todo):
        self.todo = todo