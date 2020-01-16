# -*- coding: UTF-8 -*-

import requests
import time
import random
import os
import json
import re


def starts(url, params, cookie):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': 'joucks.cn:3344',
        'Origin': 'http://joucks.cn:3344',
        'Referer': 'http://joucks.cn:3344/',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        resp = requests.post(url, headers=headers, data=params, timeout=15)
        return json.loads(resp.text)
    except Exception as e:
        return e


dir = os.path.dirname(os.path.abspath(__file__))
f = open(dir+'/key.txt', 'r')
cbmids = f.read().splitlines()
cookies = [
    'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiMTA5NjMxOTg1OEBxcS5jb20iLCJpZCI6IjVlMDAzMmNlZTNiNWFjMzMwODYxOTM0ZSIsImlhdCI6MTU3NzI1NDIwMSwiZXhwIjoxNTc5ODQ2MjAxfQ.xkHu9r0yf5bUJ9EXTJQIWXCJlCIBllgWyaxRl27_lww;',
	'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiY2hlbjBtaW5nMTIzQHFxLmNvbSIsImlkIjoiNWUwMDc2ZjdmYjdiMTIxNmYzZGZlMDJiIiwiaWF0IjoxNTc3MjU0NDgyLCJleHAiOjE1Nzk4NDY0ODJ9.jNzS1buawgZIcrxNMDsrkht9-Fm6EDX_FfaMHOOI4EE;',
	'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9uYW1lIjoiY2hlbm1pbmcyNTQ4QHFxLmNvbSIsImlkIjoiNWUwMDdkYmYyMTA2ZTExNmY5MmI2NDE4IiwiaWF0IjoxNTc3NDIzODE1LCJleHAiOjE1ODAwMTU4MTV9.eW-JODX-x8DxB5KFrClqriroMFmg3mPOp4QwnSpYQsM;'
]

# 读取key

for cbmid in cbmids:
    print(cbmid)
    times = random.randint(0, 1)
    url = 'http://joucks.cn:3344/api/exchangeVolume'
    recom = re.compile(r'"(.*?)" : "(.*?)"')
    m = recom.search(cbmid)
    code = m.group(2)
    #recom = re.compile(r'"(.*?)"')
    #m = recom.findall(cbmid)
    #code = m[3]
    #print(code)

    params = {
        'volume': code
    }
    if len(cookies) < 1:
        print("未配置cookie或任务已执行完毕")
        exit()
    for cookie in cookies:
        res = starts(url, params, cookie)
        if not isinstance(res, dict):
            print(res)
            exit()
        if res['code'] == 200 or res['code'] == 401:
            cookies.remove(cookie)
        print(res['msg'])
    time.sleep(times)
    print('-----------等待%d秒-------' % (times))