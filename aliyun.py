import requests
import datetime

class AliyunSignIn(object):
    def __init__(self, refresh_tokens):
        self.refresh_tokens = refresh_tokens

    def get_access_token(self, refresh_token):
        url = 'https://auth.aliyundrive.com/v2/account/token'
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        data = {
            "grant_type": "refresh_token",
            "app_id": "pJZInNHN2dZWk8qg",
            "refresh_token": refresh_token
        }
        res = requests.post(url, headers=headers, json=data)
        if res.status_code == 200:
            access_token = f'Bearer {res.json()["access_token"]}'
            nick_name = res.json()['nick_name']
            return access_token, nick_name
        return None, None

    def sign_in(self):
        for refresh_token in self.refresh_tokens:
            access_token, nick_name = self.get_access_token(refresh_token)
            if access_token:
                print(f'access_token获取完成，{access_token}欢迎{nick_name}\n开始签到')
                url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
                headers = {
                    "Content-Type": "application/json",
                    'Authorization': access_token,
                    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'
                }
                data = {}
                res = requests.post(url, headers=headers, json=data)
                if res.status_code == 200 and res.json()['success']:
                    res_json = res.json()
                    notice = ''
                    prefix = ''
                    for l in res_json['result']['signInLogs']:
                        if l['status'] != 'miss':
                            prefix = f'第{l["day"]}天'
                            notice = l['notice'] or ''
                            if l['reward'] and l['reward']['description']:
                                notice += ' ' + l['reward']['description']
                    notifyStr = f'{prefix}签到成功'
                    if notice:
                        notifyStr += f',获得【{notice}】'
                    print(notifyStr)
                else:
                    print(f'获取access_token失败, refresh_token: {refresh_token}')
            else:
                print(f'获取access_token失败, refresh_token: {refresh_token}')

if __name__ == '__main__':
    refresh_tokens = ['token1', 'token2']
    ali = AliyunSignIn(refresh_tokens)
    ali.sign_in()