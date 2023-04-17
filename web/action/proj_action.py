from app.db.db_helper import DBHelper
from app.db.models import Project
from datetime import datetime
from app.utils.token_parse import get_token_user_id


class ProjUtil:
    _db_helper = DBHelper()
    def create_proj(self, data=None):
        _proj = Project()
        _proj.title = data.get('title')
        # 分类允许不存在
        if not all(data.get('classify_id')):
            _proj.classify_id = data.get('classify_id')
        _proj.create_time = datetime.now()
        _proj.modify_time = _proj.create_time

        # _proj_id = data.get('proj_id')
        token = data.get('token')
        create_user = get_token_user_id(token)
        if create_user[0] == True:
            return {'code': 304, 'success': False, 'msg': "用户是谁呢"}

        _proj.create_user = create_user[1]
        _proj.modify_user = _proj.create_user
        _proj.intro = data.get('intro')
        _proj.is_del = 0
        _proj.state = int(data.get('state'))
        _proj.type = int(data.get('type'))
        if _proj.type == 2:
            _proj.passwd = data.get('passwd')
        self._db_helper.insert_proj(_proj)

        return {'code': 200, 'success': True, 'msg': "创建文集成功", 'proj_id': _proj.id}
