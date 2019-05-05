from crawl_guazi.common import *


def parse_cookies(origin_cookies, str_cookies):
    """
    解析cookie并重新设置新值
    """
    cookie = origin_cookies
    for i in range(0, len(str_cookies)):
        temp = str(str_cookies[i], encoding="utf8").split(';')[0].split('=')
        if temp[1] == 'null':
            # if temp[1] in cookie.keys():
            #     cookie.pop(temp[1])
            continue
        cookie[temp[0]] = temp[1]
    return cookie
