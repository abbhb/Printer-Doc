from threading import Lock
import os

DATA_SOURCE = {
    "default": {
        "name": "mysql",  # 数据引擎名称
        "username": "root",
        "password": "123456",
        "host": "192.168.12.12",
        "port": "3306",
        "database": "doc"
    },
}
CACHE = {
    "default": {
        "host": "192.168.12.12",
        "port": "6379",
        "database": "0"
    }
}
SECRET_KEY = "reggit20230113.FfG!D3a2AcfrF.2u0C1"


class DOC_STATE:
    PUBLIC = 1
    draft = 0


# 线程锁
lock = Lock()

# 全局实例
_CONFIG = None


def SingleConfig(cls):
    """单例装饰器"""

    def _single_config(*args, **kwargs):
        global _CONFIG
        if not _CONFIG:
            with lock:
                # 初次运行, 给_CONFIG变量赋值
                _CONFIG = cls(*args, **kwargs)
        return _CONFIG

    return _single_config


@SingleConfig
class Setting(object):
    _config = {}

    def __init__(self):
        if not os.environ.get('TZ'):
            os.environ['TZ'] = 'Asia/Shanghai'

    @staticmethod
    def get_data_source_url():
        data_source = DATA_SOURCE.get("default")
        sql_name = data_source.get('name')
        username = data_source.get('username')
        password = data_source.get('password')
        host = data_source.get('host')
        port = data_source.get('port')
        database = data_source.get('database')
        return f"{sql_name}+pymysql://{username}:{password}@{host}:{port}/{database}"

    @staticmethod
    def get_cache_source_url():
        cache = CACHE.get("default")
        host = cache.get("host")
        port = cache.get("port")
        database = cache.get("database")
        return f"redis://{host}:{port}/{database}"
