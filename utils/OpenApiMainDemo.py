# python OpenApi调用demo  V0.0.1
# author baiying
# date 2018/12/04

import hmac
import base64
import urllib
import datetime
import urllib.request
import urllib.parse

'''
 Demo说明：
     本demo为python调用百应openApi的基础demo
     目前只提供获取公司列表号码的demo用例
     主要提供百应接口访问的签名算法
'''

# ak 需要获取
appKey = '****APPKey*****'
appSecrete = '*****APPSECRET*****'

# GMT时间获取
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
time_format_gmt = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime(GMT_FORMAT)

# 签名计算
signMessage = appKey + '\n' + time_format_gmt
quote = base64.b64encode(
    hmac.new(bytes(appSecrete.encode("utf-8")), bytes(signMessage.encode("utf-8")), digestmod='sha1')
        .digest()).decode("utf-8")

# 百应线上环境api访问地址
BASE_URL = "http://api.byrobot.cn"


def get_companys():
    request_obj = urllib.request.Request(url=BASE_URL + "/openapi/v1/company/getCompanys")
    request_obj.add_header("sign", quote)
    request_obj.add_header("datetime", time_format_gmt)
    request_obj.add_header("appkey", appKey)
    response_obj = urllib.request.urlopen(request_obj)
    html_code = response_obj.read().decode('utf-8')
    return html_code


companys = get_companys()
print(companys)
