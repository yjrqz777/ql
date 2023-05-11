import requests
import time

url = 'https://promotion.waimai.meituan.com/lottery/limitcouponcomponent/fetchcoupon'
cookies = 'com.sankuai.passport.login.component_random=; com.sankuai.passport.login.component_strategy=; backurl=https://i.meituan.com/account; _lxsdk_cuid=187d6d499e2c8-03bd540d9e9c32-26031b51-1fa400-187d6d499e2c8; WEBDFPID=1u70z48u1517538wy81802x91444yy2x812w3w50uw19795832vyvwu2-1998296470426-1682936470426WOEUMWUfd79fef3d01d5e9aadc18ccd4d0c95073963; iuuid=87F308E9B062B1C80B6787EF91A466D976F70FB8B6B6A34FB0B955E5FE8FB492; token=AgHMIlRacRrhtG84DY94Cf-l675QT8ohAmOnCuXE5heNfOr8TP5QH-7sifbSh-4EF3WZQISKQ83_WQAAAAAtGAAA_6RqE5noip5XJHr_7Aqjn7Hw2hX9-Dw_JtwNhKl-FrYMH2RdKNrEehxSRTcY40nD; mt_c_token=AgHMIlRacRrhtG84DY94Cf-l675QT8ohAmOnCuXE5heNfOr8TP5QH-7sifbSh-4EF3WZQISKQ83_WQAAAAAtGAAA_6RqE5noip5XJHr_7Aqjn7Hw2hX9-Dw_JtwNhKl-FrYMH2RdKNrEehxSRTcY40nD; oops=AgHMIlRacRrhtG84DY94Cf-l675QT8ohAmOnCuXE5heNfOr8TP5QH-7sifbSh-4EF3WZQISKQ83_WQAAAAAtGAAA_6RqE5noip5XJHr_7Aqjn7Hw2hX9-Dw_JtwNhKl-FrYMH2RdKNrEehxSRTcY40nD; userId=2916346838; isid=AgHMIlRacRrhtG84DY94Cf-l675QT8ohAmOnCuXE5heNfOr8TP5QH-7sifbSh-4EF3WZQISKQ83_WQAAAAAtGAAA_6RqE5noip5XJHr_7Aqjn7Hw2hX9-Dw_JtwNhKl-FrYMH2RdKNrEehxSRTcY40nD; uuid=563d4723513048d4b9fe.1682936586.1.0.0; _lxsdk=87F308E9B062B1C80B6787EF91A466D976F70FB8B6B6A34FB0B955E5FE8FB492; _lxsdk_s=187d6d499e3-211-604-519||13; ci=73; qruuid=a876e7d9-863f-4151-b235-6f9379a793c9'
data = {
    'couponReferId': '5865AE2DF47846FC8C2B85078C075051',
    'actualLng': '108.674404',
    'actualLat': '19.042169',
    'geoType': '2',
    'gdPageId': '481021',
    'pageId': '482299',
    'version': '1',
    'utmSource': '',
    'utmCampaign': '',
    'instanceId': '16825614060250.5872321938318412',
    'componentId': '16825614060250.5872321938318412'
}
headers = {
    'Connection': 'keep-alive',
    'Content-Length': '2528',
    'Accept': 'application/json, text/plain, */*',
    #1682748007000
    #1682916907546
    'mtgsig': '{"a1":"1.0","a2":"1682748007000","a3":"uz3x8y4zzw495w70z472yyvzuuuxxv60812w4z3vz1u97958xy0135x4","a4":"0a4f3202ad50b67002324f0a70b650ad1828e5df689eb572","a5":"0qaELmW6gNAtJ7UTvaEq2G+VbqmH0MnuUxCQmC3bKfSxrDipZqHjVi4n0R3dB/Q2XJPCt7EAt82ljzJWh9TkAiGZhMh=","a6":"h1.2lYyNgvWjVsY3R5qksEQaR02Z5U4NNrVWWdWTvKuqBhs6VR3ODuxFpxWDiWLYMUvVqeNOMn5KQ5lKaULHYhNnzGq2Vjm6JBmopLylo82ckrbk26GebBgZhTTreAx0a/uSFiWE1EzQ3vL3akVMgRgkgW076CsToe4ubeBHB70XPkiHI3QDtA9/Y+BNegH+GWQTRCcLYDcyrLlqBUKw4bwIsRf7zWldZEEdeo8Cuenm+lR+uxmLFFYtjijkWVGkI+ZhfrUp0g9jXMlr01YvEehraplssI3AwMxwMO58a1sB2FBGv6p+o6mx9SSLZ9d3uc56nkozvVUEud4oRum0SVa+RPiv/CNnn83cxbcQNMVQJdzwFt9UmF9KrG/HE5pD/FSMYVGCDfsqhPwGMTFdioRPAOl2Fbg+o0ZRyh+5u25gF90SzMOONPCS2TuLYxOVn3AO","a7":"","x0":4,"d1":"fc91455ad9cef39a8e5ff71b40420d3e"}',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K30i 5G Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.40423 swan-mibrowser',
    'Content-Type': 'application/json',
    'Origin': 'https://market.waimai.meituan.com',
    'Referer': 'https://market.waimai.meituan.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': cookies,
}
json_data = {
    "cType": "mti",
    "fpPlatform": 3,
    "wxOpenId": "",
    "appVersion": "",
    "mtFingerprint": "H5dfp_1.8.2_tttt_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"}
msg = ''
while '成功' not in msg:
    response = requests.post(url, headers=headers, params=data, json=json_data)
    msg = response.json().get('msg')
    print('msg：', msg)
    if '已领取' or '来晚了' in msg:
        print('留点机会给年轻人吧！msg：', msg)
        break
    time.sleep(0.03)
else:
    print('领取成功，msg为：', msg)

