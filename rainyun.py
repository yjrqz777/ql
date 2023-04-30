# coding=utf-8
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path
import logging
import json
import notify


# messages=''


class RainYun():

    def __init__(self, user: str, pwd: str) -> None:

        # 认证信息
        self.user = user.lower()
        self.pwd = pwd
        self.json_data = json.dumps({
            "field": self.user,
            "password": self.pwd,
        })
        # messages=self.user+'\t'
        # 日志输出
        self.logger = logging.getLogger(self.user)
        formatter = logging.Formatter(datefmt='%Y/%m/%d %H:%M:%S',
                                      fmt="%(asctime)s 雨云 %(levelname)s: 用户<%(name)s> %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        # 签到结果初始化
        self.signin_result = False
        # 请求设置
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "",
            "Origin": "https://api.rainyun.com",
            "Referer": "https://api.rainyun.com"
        })
        self.login_url = "https://api.v2.rainyun.com/user/login"
        self.signin_url = "https://api.v2.rainyun.com/user/reward/tasks"
        self.logout_url = "https://api.v2.rainyun.com/user/logout"
        self.query_url = "https://api.v2.rainyun.com/user/"

    # messages=user.lower()+'\t'
    def login(self) -> None:
        """登录"""
        res = self.session.post(
            url=self.login_url, headers={"Content-Type": "application/json"}, data=self.json_data)
        if res.text.find("200") > -1:
            self.logger.info("登录成功")
            # messages=messages+'\n'+'登录成功'
            self.session.headers.update({
                "X-CSRF-Token": res.cookies.get("X-CSRF-Token", "")
            })
        else:
            self.logger.error(f"登录失败，响应信息：{res.text}")
            # messages=messages+'\n'+f"登录失败，响应信息：{res.text}"

    def signin(self) -> None:
        """签到"""
        res = self.session.post(url=self.signin_url, headers={"Content-Type": "application/json"}, data=json.dumps({
            "task_name": "每日签到",
            "verifyCode": ""
        }))
        self.signin_date = datetime.utcnow()
        if res.text.find("200") > -1:
            self.logger.info("成功签到并领取积分")
            # messages=messages+'\n'+'成功签到并领取积分'
            self.signin_result = True
        else:
            self.logger.error(f"签到失败，响应信息：{res.text}")
            # messages=messages+'\n'+f"签到失败，响应信息：{res.text}"
            notify.send("【雨云签到】", f"签到失败，响应信息：{res.text}-登录失败 ")
            self.signin_result = False

    def logout(self) -> None:
        res = self.session.post(url=self.logout_url)
        if res.text.find("200") > -1:
            self.logger.info('已退出登录')
            # messages=messages+'\n'+'已退出登录'
        else:
            self.logger.warning(f"退出登录时出了些问题，响应信息：{res.text}")
            # messages=messages+'\n'+f"退出登录时出了些问题，响应信息：{res.text}"

    def query(self) -> None:
        res = self.session.get(url=self.query_url)
        self.points = None
        if res.text.find("200") > -1:
            data = res.json()["data"]
            self.points = data.get("Points", None) or data["points"]
            self.logger.info(
                f"积分查询成功为 {self.points} 约等价于 {round(self.points / 2000, 2)} ¥")
            # messages=messages+'\n'+ f"积分查询成功为 {self.points} 约等价于 {round(self.points/2000,2)} ¥"
            notify.send("雨云签到",
                        f" {self.signin_result} 积分查询成功为 {self.points} 约等价于 {round(self.points / 2000, 2)} ¥")
        else:
            self.logger.error(f"积分信息失败，响应信息：{res.text}")
            # messages=messages+'\n'+f"积分信息失败，响应信息：{res.text}"
        # notify.send('雨云签到',messages)

    def log(self, log_file: str, max_num=5) -> None:
        """存储本次签到结果的日志"""
        # 北京时间
        time_string = self.signin_date.replace(tzinfo=timezone.utc).astimezone(
            timezone(timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
        file = Path(log_file)
        record = {
            "date": time_string,
            "result": self.signin_result,
            "points": self.points
        }
        previous_records = {}
        if file.is_file():
            try:
                with open(log_file, 'r') as f:
                    previous_records = json.load(f)
                if not previous_records.get(self.user):
                    previous_records[self.user] = []
                previous_records[self.user].insert(0, record)
                previous_records[self.user] = previous_records[self.user][:max_num]
            except Exception as e:
                self.logger.error("序列化日志时出错：" + repr(e))
        else:
            previous_records[self.user] = [record]
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(previous_records, f, indent=4)
        self.logger.info('日志保存成功')


if __name__ == '__main__':
    accounts = [
        {
            "user": "1111",  # 账户
            "password": "11111.."  # 密码
        },
        {
            "user": "11111",  # 账户
            "password": "111111.."  # 密码
        }
    ]
    for acc in accounts:
        ry = RainYun(acc["user"], acc["password"])  # 实例
        ry.login()  # 登录
        ry.signin()  # 签到
        ry.query()  # 查询积分
        ry.logout()  # 登出
        # 保存日志则打开注释 推荐文件绝对路径
        # file = "./rainyun-signin-log.json"
        # 日志最大记录数量
        # max_num = 5
        # ry.log(file, max_num)  # 保存日志