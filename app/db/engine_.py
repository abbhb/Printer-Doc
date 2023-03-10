from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from setting import Setting
from app.utils.exception_utils import ExceptionUtils


# engine = create_engine('mysql://username:password@localhost/database_name')
_Engine = create_engine(
    Setting().get_data_source_url(),
    pool_size=20
)
_Session = scoped_session(sessionmaker(bind=_Engine,
                                       autoflush=True,
                                       autocommit=False,
                                       expire_on_commit=False))


class MainDB:

    @property
    def session(self):
        return _Session

    def query(self, *obj):
        """查询对象"""
        return self.session.query(*obj)

    def insert(self, data):
        """
        插入数据

        :param data: 待插入到数据库中的数据
        """
        if isinstance(data, list):
            self.session.add_all(data)
        else:
            self.session.add(data)

    def execute(self, sql):
        """执行sql语句"""
        print(sql)
        return self.session.execute(text(sql))

    def flush(self, ):
        """flush 的意思就是将当前 session 存在的变更发给数据库，换句话说，就是让数据库执行 SQL 语句"""
        self.session.flush()

    # SQLAlchemy 在执行 commit 之前，肯定会执行 flush 操作；而在执行 flush 的时候，不一定执行 commit
    def commit(self):
        """commit 的意思是提交一个事务。一个事务里面可能有一条或者多条 SQL 语句"""
        self.session.commit()

    def rollback(self):
        """回滚事务"""
        self.session.rollback()


class DBPersist(object):
    """数据库持久化装饰器, 其实就是方法执行完自动commit一下, 然后有问题就回滚"""

    def __init__(self, _db):
        self.db = _db

    def __call__(self, f):
        def persist(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
                self.db.commit()
                return True if ret is None else ret  # 方法执行结果为空, 返回True
            except Exception as e:
                # 打印异常堆栈信息, 回滚
                ExceptionUtils.exception_traceback(e)
                self.db.rollback()
                return False

        return persist


if __name__ == '__main__':
    print(Setting().get_data_source_url())
    print(MainDB.session)
    from app.db.models import Doc

    db = MainDB()
    results = db.query(Doc).all()
    # for i in range(5):
    #     print(results[i])

    result = db.execute("select * from doc where id=3")
    print(type(result))
    print(result.all())
