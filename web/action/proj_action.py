from app.db.db_helper import DBHelper
from app.db.models import Project
from datetime import datetime
from setting import DOC_STATE


class ProjUtil:
    _db_helper = DBHelper()

    def create_proj(self, data=None):
        _proj = Project()
        _proj.title = data.get('title')
        _proj.content = data.get('content')
        # _proj_id = data.get('proj_id')
        token = data.get('token')
        # parse token

        # if not self._db_helper.select_proj_by_id(_proj_id).all():
        #     return {'code': 304, 'success': False, 'msg': "文集不存在"}
        #
        # _doc.proj_id = _proj_id
        # _doc.version = 1
        # _doc.create_time = datetime.now()
        # _doc.modify_time = _doc.create_time
        # _doc.create_user = token
        # _doc.modify_user = _doc.create_user
        # _doc.is_del = False
        # _doc.state = DOC_STATE.PUBLIC
        # self._db_helper.insert_doc(_doc)
        return {'code': 200, 'success': True, 'msg': "创建文集成功", 'proj_id': _proj.id}
