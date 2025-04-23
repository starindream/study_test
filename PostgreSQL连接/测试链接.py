from sqlalchemy import create_engine, String, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker, scoped_session
from datetime import datetime

engine = create_engine(
    'postgresql+psycopg://guanjunhao:123456@localhost:5432/postgres')

# engine = create_engine('mysql+pymysql://root:a123456789@localhost/demo')


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = 'test'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    create_time: Mapped[str] = mapped_column(DateTime, nullable=False)


class Emp(Base):
    __tablename__ = 't_emp'

    empno: Mapped[int] = mapped_column(primary_key=True)
    ename: Mapped[str] = mapped_column(String(50))
    deptno: Mapped[int] = mapped_column(ForeignKey('t_dept.deptno'))
    hiredate: Mapped[str] = mapped_column(String(50))

    dep = relationship("Dep", backref="emp")


class Dep(Base):
    __tablename__ = 't_dept'

    deptno: Mapped[int] = mapped_column(primary_key=True)
    dname: Mapped[str] = mapped_column(String(50))
    loc: Mapped[str] = mapped_column(String(50))


session_factory = sessionmaker(bind=engine)

# 每次在调用 _session.add 时，会在内部先调用返回 session 的实例中的 registry 生成一个新的session，再进行使用
# _session = scoped_session(session_factory=session_factory)

DBSession = scoped_session(session_factory=session_factory)


def search_emp():
    session = DBSession()

    sql = session.query(Emp)
    result = sql.all()

    res = []

    for item in result:
        new_item = item.__dict__
        res.append(new_item)

    print('result', result)
    print('res', res)


def search_test():
    session = DBSession()
    query = session.query(Test)
    res = query.all()

    result = []

    for item in res:
        new_item = item.__dict__
        result.append(new_item)
    print('result', result)


def str_time_compare():
    session = DBSession()
    time = '2025-01-22 00:00:00'
    time_2 = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    print('time2', time_2)
    filter = [Test.create_time <= time_2]
    query = session.query(Test).where(*filter)
    result = query.all()
    for i in result:
        print(i.__dict__)
    print('result', result)


def create_test():
    session = DBSession()
    one = Test(id=1, name='one1', create_time='2025-01-22 00:00:00')
    two = Test(id=2, name='two2', create_time='2025-01-23 00:00:00')
    session.add_all([one, two])
    session.commit()
    session.close()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # search_emp()
    # search_test()
    str_time_compare()
    # create_test()
