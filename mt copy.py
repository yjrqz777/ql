import requests
import time
import datetime
import notify

#coding:UTF-8
import time

dt = "2016-05-05 20:28:54"

#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)




def stamp_to_time(stamp):
    stamps = stamp
    time = datetime.datetime.fromtimestamp(stamps)
    return time
def time_to_stamp(times):

    dt = "2016-05-05 20:28:54"
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp
url2="https://bbs.binmt.cc/plugin.php"
paramss={
'id':f'k_misign:sign',
'operation':'qiandao',
'format':'text',
'formhash':'dc76e28f'
}
#url="https://bbs.binmt.cc/plugin.php?id=k_misign&sign&operation=qiandao&format=text&formhash=dc76e28f"
cookie=f'cQWy_2132_saltkey=tO2ScCu2;\
        cQWy_2132_lastvisit={4};\
        cQWy_2132_ulastactivity=19c******************************************y66Jy62ZQTBmm;\
        cQWy_2132_auth=eeb5KSB*************************************************************RkAUTxA7tl;\
        cQWy_2132_lastcheckfeed=7373%7C{3};\
        cQWy_2132_comiis_homestyleid_u7373=yes%2Ahome_bg.jpg;\
        cQWy_2132_connect_is_bind=1;\
        cQWy_2132_home_diymode=1;\
        cQWy_2132_atarget=1;\
        cQWy_2132_visitedfid=44;\
        cQWy_2132_clearUserdata=forum;\
        cQWy_2132_viewid=tid_109852;\
        guardret=pKfrQw0************2ckGqQ==;\
        cQWy_2132_comiis_coloruid_7373=0s;\
        cQWy_2132_st_p=7373%7C{2}%7C6e*********************09bfbb23b96;cQWy_2132_sid=oy6i6z;\
        cQWy_2132_lip=182.118.238.88%2C1683597568;\
        cQWy_2132_st_t=7373%7C{0}%7C*******************cc45d534;\
        cQWy_2132_forum_lastvisit=D_44_{0};\
        cQWy_2132_checkpm=1;cQWy_2132_lastact={1}%09plugin.php%09'.format(int(time.time()),\
                                                                          int(time.time())+2000,\
                                                                            int(time.time())-2000,\
                                                                                int(time.time())-4000,\
                                                                                    int(time.time())-6000)

data={
'Host': 'bbs.binmt.cc',
'accept': f'text/plain, */*; q=0.01',
'user-agent': f'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 BingWeb/6.9.6',
'x-requested-with': 'XMLHttpRequest',
'sec-fetch-site': f'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://bbs.binmt.cc/k_misign-sign.html',
'accept-encoding': f'gzip, deflate',
'accept-language': f'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':cookie
}

def main_handler():
    res=requests.get(url=url2,params=paramss,headers=data)
    if "已签到" in res.text:
        print(stamp_to_time(int(time.time())),"已签到")
        notify.send("MT论坛", "已签到")
    elif "今日已签" in res.text:
        print(stamp_to_time(int(time.time())),"签过了")
        notify.send("MT论坛", "签过了")
    else:
        print("出现未知错误"+res.text)
        notify.send("MT论坛", "出现未知错误"+res.text)
if __name__ == '__main__':
    main_handler()