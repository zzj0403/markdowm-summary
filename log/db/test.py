from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.mould import *

engine = create_engine(
    "mysql+pymysql://zzj:4dAnFoLdh7mB39yCp76E@47.97.44.176:13006/test?charset=utf8",
    max_overflow=5,
    pool_size=5,
    pool_timeout=10,
    pool_recycle=-1, )

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()
