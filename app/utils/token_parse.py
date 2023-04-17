import base64


def get_token_user_id(token):
    s = token.split(".")[1]
    s += "=" * ((4 - len(s) % 4) % 4)
    print(eval(str(base64.urlsafe_b64decode(s), encoding="utf8")))
    return eval(str(base64.urlsafe_b64decode(s), encoding="utf8"))["id"]