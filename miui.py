#变量名   miui
#值       账号:密码

import requests
import os
import urllib3
import http.cookies
import re

urllib3.disable_warnings()

credentials = os.environ.get('miui')
if credentials:
  for credential in credentials.split('#'):
    username, userpass = credential.split(':')
    print('账号:', username)

headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'miuiver.com',
}

data = {
    'log': username,
    'pwd': userpass,
    'action': 'mobantu_login',
}


response = requests.post('https://miuiver.com/wp-content/plugins/erphplogin//action/login.php', headers=headers, data=data, verify=False)

cookie_value = re.findall(r'wordpress_logged_in_\w+[^;]+', response.headers['Set-Cookie'])[0]

cookies = {'wordpress_logged_in': cookie_value}

headers2 = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    'cookie': cookie_value ,
    'Host': 'miuiver.com',
}

data2 = {
    'action': 'epd_checkin',
}
response2 = requests.post('https://miuiver.com/wp-admin/admin-ajax.php', headers=headers2, data=data2, verify=False)

if response2.status_code == 200:
    result = response2.json()
    if result['status'] == 201:
        print('已经签到过了')
    elif result['status'] == 200:
        print('已签到')
    else:
        print('签到失败')
else:
    print(response2.text)