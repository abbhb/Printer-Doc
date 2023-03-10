import re


# HTML转义
def jsonXssFilter(data):
    payloads = {
        '\'': '&apos;',
        '"': '&quot;',
        '<': '&lt;',
        '>': '&gt;'
    }
    if type(data) == dict:
        new = {}
        for key, values in data.items():
            new[key] = jsonXssFilter(values)
    elif type(data) == list:
        new = []
        for i in data:
            new.append(jsonXssFilter(i))
    elif type(data) == int or type(data) == float:
        new = data
    elif type(data) == str:
        new = data
        for key, value in payloads.items():
            new = new.replace(key, value)
    elif type(data) == bytes:
        new = data
    else:
        # print('>>> unknown type:')
        # print(type(data))
        new = data
    return new


def html_filter(data):
    if len(data) == 0:
        return ""
    payloads = {
        '\'': '&apos;',
        '"': '&quot;',
        '<': '&lt;',
        '>': '&gt;'
    }
    new = data
    for key, value in payloads.items():
        new = new.replace(key, value)
    print(new)
    return new


# 替换前端传来的非法字符
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|\[\]]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title
