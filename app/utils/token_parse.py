import jwt

from setting import SECRET_KEY


def get_token_user_id(token):
    failed = False
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(data)
        return failed,data["id"]
    except Exception as e:
        failed = True
        return failed,e

if __name__ == '__main__':
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZXJtaXNzaW9ucyI6IjEiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTY0MDcxNTAyOTQ0NDI1OTg0MSIsInV1aWQiOiIwYmE0YTc1ZTVlOGY0ZGEwYTQxMzJkZmJhNTc1NWE4MSJ9.YEtzQgOeBdJnV3u7E0agoetl7oBCw24f_ZidM50Cgig"
    print(get_token_user_id(token))