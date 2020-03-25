from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Enum, ForeignKey, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship

import datetime

Base = declarative_base()


#


class log(Base):
    __tablename__ = 'total_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime, nullable=False)
    ip = Column(String(32), nullable=False)
    method = Column(String(32), default=None )
    request = Column(Text, default=None)
    stat_code = Column(Integer, default=None)
    boy_size = Column(Integer, default=None)
    request_body = Column(Text, default=None)
    user_agent = Column(String(32), default=None)
    request_time = Column(Float, default=None)
    correct_log = Column(Enum('0', '1'), default='0', nullable=False)
    project = Column(String(32), nullable=False)

    lp = relationship("project",backref='pers')

# class project(Base):
#     __tablename__ = 'project_name'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     project_name = Column(String(32), nullable=False)
# class test(Base):
#     __tablename__ = 'test'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(32), nullable=False)


def init_db():
    engine = create_engine(
        "mysql+pymysql://zzj:4dAnFoLdh7mB39yCp76E@47.97.44.176:13006/test?charset=utf8",
        max_overflow=5,
        pool_size=5,
        pool_timeout=10,
        pool_recycle=-1,

    )
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
