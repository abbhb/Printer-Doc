from app.db.engine_ import MainDB, DBPersist
from app.db.models import Doc, Project


class DBHelper:
    _db = MainDB()

    @DBPersist(_db)
    def insert_doc(self, doc):
        """新建文档"""
        self._db.insert(doc)

    def select_proj_by_id(self, _id):
        return self._db.query(Project).filter(Project.id == _id)


if __name__ == '__main__':
    dbh = DBHelper()
    result = dbh.select_proj_by_id(12)
    print(result.all())
