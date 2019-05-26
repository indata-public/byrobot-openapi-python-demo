# python OpenApi调用demo  V0.0.1
# author baiying
# date 2018/12/04

import hmac
import base64
import urllib
import datetime
import urllib.request
import urllib.parse
import json

'''
 Demo说明：
     本demo为python调用百应openApi的基础demo
     目前只提供获取公司列表号码的demo用例
     主要提供百应接口访问的签名算法
'''

# ak 需要获取
appKey = '****APP_KEY*****'
appSecrete = '*****APP_SECRET*******'

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


def get_phones():
    request_obj = urllib.request.Request(url=BASE_URL + "/openapi/v1/company/getPhones?companyId=3813")
    request_obj.add_header("sign", quote)
    request_obj.add_header("datetime", time_format_gmt)
    request_obj.add_header("appkey", appKey)
    response_obj = urllib.request.urlopen(request_obj)
    html_code = response_obj.read().decode('utf-8')
    return html_code


def post_create_job():
    textmod = {
          "companyId" : 3813,
          "taskName" : "测试任务",
          "taskType" : 2,
          "startDate" : "2017-10-19",
          "workingStartTime" : "08:00",
          "workingEndTime" : "22:00",
          "breakStartTime":"12:00",
          "breakEndTime":"14:00",
          "userPhoneIds" : [20121],
          "callType" : 1,
          "concurrencyQuota" :1,
          "robotDefId" : 1,
          "sceneDefId" : 1,
          "sceneRecordId" : 7,
          "remark" : "创建任务",
          "userLevelPush": "用户自定义推送参数"
      }
    textmod = json.dumps(textmod).encode(encoding='utf-8')
    print(textmod)
    header_dict = {"Content-Type": "application/json"}
    req = urllib.request.Request(url=BASE_URL+'/openapi/v1/task/createTask', data=textmod, headers=header_dict)
    req.add_header("sign", quote)
    req.add_header("datetime", time_format_gmt)
    req.add_header("appkey", appKey)
    res = urllib.request.urlopen(req)
    res = res.read()
    print(res)
    print(res.decode(encoding='utf-8'))


companys = get_companys()
print(companys)


post_create_job()


phones = get_phones()
print(phones)

