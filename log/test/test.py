from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Enum
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://zzj:4dAnFoLdh7mB39yCp76E@47.97.44.176:13006/test?charset=utf8'",
                       max_overflow=5,
                       echo=True,
                       )
# engine.connect()
Base = declarative_base()


class log_table(Base):
    __tablename__ = 'test1'
    id = Column(Integer, index=True, primary_key=True)
    date = Column(DateTime)
    ip = Column(String(32))
    method = Column(String(32))
    request = Column(String(64))
    stat_code = Column(Integer)
    boy_size = Column(Integer)
    request_body = Column(String(64))
    user_agent = Column(String(32))
    request_time = Column(Float)
    Correct_log = Column(Enum('0', '1'), default=1)


def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()
