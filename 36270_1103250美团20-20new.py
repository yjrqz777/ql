import requests
import time

url = 'https://bbs.binmt.cc/member.php'
data = {
    'mod':'logging',
    'action':'login',
    'loginsubmit':'yes',
    'loginhash':'Lxkhr',
    'handlekey':'loginform',
    'inajax':'1'
}
headers = {
    'Host': 'bbs.binmt.cc',
    'content-length': '176',
    'accept': f'application/xml, text/xml, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': f'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 BingWeb/6.9.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://bbs.binmt.cc',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://bbs.binmt.cc/member.php?mod=logging&action=login&mobile=2',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': f'guardret=pKfrQw0hLnjQIoDv2ckGqQ==;\
                cQWy_2132_saltkey=dsDshddb;\
                cQWy_2132_lastvisit=1683767146;\
                cQWy_2132_sid=F2kB4k;\
                cQWy_2132_lastact=1683905582%09member.php%09logging'
}
json_data = {
    'formhash':'4c5a63f4',
    'referer':f'https%3A%2F%2Fbbs.binmt.cc%2F.%2F',
    'fastloginfield':'username',
    'cookietime':'31104000',


    'username':'yjrqz777',
    'password':'Cduan2001..',
    'questionid':'0',
    'answer':'',
    'agreebbrule':''
}


if __name__ == '__main__':
    response = requests.post(url, headers=headers, params=data, data=json_data)
    cookies = response.cookies
    #response.
    print(cookies,end='\n')
    print(response.text,end='\n')
