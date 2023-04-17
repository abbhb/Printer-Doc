from flask import Blueprint, request
from flask_restx import Api, reqparse, Resource

from web.action.proj_action import ProjUtil
from web.security import require_token
from web.action.doc_action import DocUtil

# from app.brushtask import BrushTask
# from app.rsschecker import RssChecker
# from app.sites import Sites
# from app.utils import TokenCache
# from config import Config
# from web.action import WebAction
# from web.backend.user import User
# from web.security import require_auth, login_required, generate_access_token

api_v1_bp = Blueprint(
    "api_v1",
    __name__,
    static_url_path='',
    static_folder='./frontend/static/',
    template_folder='./frontend/',
)

Api_v1 = Api(
    api_v1_bp,
    version="1.0",
    title="NAStool Api",
    description="POST接口调用 /user/login 获取Token，GET接口使用 基础设置->安全->Api Key 调用",
    doc="/",
    security='Bearer Auth',
    authorizations={"Bearer Auth": {"type": "apiKey", "name": "Authorization", "in": "header"}},
)

# API分组
docs = Api_v1.namespace('docs', description='文档')
images = Api_v1.namespace('images', description='图片')
projects = Api_v1.namespace('projects', description='项目(文集)')


class TokenRequired(Resource):
    """需要token"""
    # method_decorators = [require_token, ]
    ...


def failed(_code=-1, _msg='fail'):
    """失败信息"""
    return {
        'code': _code,
        'success': False,
        'msg': _msg
    }


def success(_code=200, _msg='success'):
    return {
        'code': _code,
        'success': True,
        'msg': _msg
    }


@docs.route("/add")
class AddDoc(TokenRequired):
    parser = reqparse.RequestParser()

    parser.add_argument('token', type=str, help='token', location='headers', required=True)
    parser.add_argument('title', type=str, help='文章标题', location='json', required=True)
    parser.add_argument('content', type=str, help='文章内容', location='json', required=True)
    parser.add_argument('proj_id', type=str, help='文集编号', location='json', required=True)

    @docs.doc(parser=parser)
    def post(self):
        """
        新建文章
        """
        args = self.parser.parse_args()
        token = args.get('token')
        title = args.get('title')
        content = args.get('content')
        proj_id = args.get('proj_id')
        if not token:
            return failed(_code=403, _msg="安全认证未通过，请检查Token")
        if not title:
            return failed(_msg='required title')
        if not content:
            return failed(_msg='required content')
        if not proj_id:
            return failed(_msg='required proj_id')

        return DocUtil().create_doc(data=args)


@projects.route("/add")
class AddProj(TokenRequired):
    parser = reqparse.RequestParser()

    parser.add_argument('token', type=str, help='token', location='headers', required=True)
    parser.add_argument('title', type=str, help='文集标题', location='json', required=True)
    parser.add_argument('classify_id', type=str, help='分类id', location='json', required=False)
    parser.add_argument('type', type=str, help='文档类型', location='json', required=True)
    parser.add_argument('state', type=str, help='文档状态', location='json', required=True)
    parser.add_argument('passwd', type=str, help='访问码', location='json', required=False)
    parser.add_argument('intro', type=str, help='文档介绍', location='json', required=False)

    @projects.doc(parser=parser)
    def post(self):
        """
        新建文集
        """
        args = self.parser.parse_args()
        token = args.get('token')
        title = args.get('title')

        classify_id = args.get('classify_id')
        type = args.get('type')
        state = args.get('state')
        passwd = args.get('passwd')
        intro = args.get('intro')
        print(args)
        if not token:
            return failed(_code=403, _msg="安全认证未通过，请检查Token")
        if not title:
            return failed(_msg='required title')
        if not type:
            return failed(_msg='required type')
        if not state:
            return failed(_msg='required state')
        if state == 2 and not passwd:
            return failed(_msg='required passwd')

        return ProjUtil().create_proj(data=args)
