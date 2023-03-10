# coding: utf-8
from sqlalchemy import Column, Float, Index, Integer, Text, text, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Doc(Base):
    __tablename__ = 'doc'
    id = Column(Integer, Sequence('id'), primary_key=True)
    title = Column(Text)
    content = Column(Text)
    proj_id = Column(Integer)
    version = Column(Integer)
    state = Column(Integer)
    create_time = Column(DateTime)
    modify_time = Column(DateTime)
    create_user = Column(Integer)
    modify_user = Column(Integer)
    is_del = Column(Integer)

    def __str__(self):
        return f"{self.id=}, {self.title=}"


class Project(Base):
    __tablename__ = "proj"
    id = Column(Integer, Sequence('id'), primary_key=True)
    title = Column(Text)
    classify_id = Column(Integer)
    is_del = Column(Integer)
    type = Column(Integer)
    create_time = Column(DateTime)
    modify_time = Column(DateTime)
    create_user = Column(Integer)
    modify_user = Column(Integer)
    state = Column(Text)
    passwd = Column(Text)
    intro = Column(Text)

    def __str__(self):
        return f"{self.id=}, {self.title=}"
