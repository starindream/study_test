from sqlalchemy import create_engine, String, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker, scoped_session

# with_entires 常用来指定返回的列，可以将 query中返回的模型进行进一步的细化，只返回特定的列


engine = create_engine('mysql+pymysql://root:a123456789@localhost/demo')

# 保存session的配置，在调用时会返回一个session来供使用
session_factory = sessionmaker(bind=engine)

# 在 session_factory 的基础上进行封装，可以实现线程安全，不同的线程调用不同的session
session_ = scoped_session(session_factory)


class Base(DeclarativeBase):
    pass


class Emp(Base):
    __tablename__ = 't_emp'

    empno: Mapped[int] = mapped_column(primary_key=True)
    ename: Mapped[str] = mapped_column(String(20))
    # 用来确定两张表之间通过哪个字段来进行联系
    deptno: Mapped[int] = mapped_column(ForeignKey('t_dept.deptno'))

    # relationship 表示在orm模型中，两个表模型之间互相存储相关联行的属性，backref 会自动在对应的表模型中，创建 emp 属性来存储 Emp 实例
    dept = relationship("Dept", backref='emp')


class Dept(Base):
    __tablename__ = 't_dept'

    deptno: Mapped[int] = mapped_column(primary_key=True)
    dname: Mapped[str] = mapped_column(String(20))
    loc: Mapped[str] = mapped_column(String(20))


def search():
    sql = session_.query(Emp)
    data = sql.all()
    total = sql.with_entities(func.count(Emp.empno)).scalar()
    print('data', data)
    print('total', total)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    search()
