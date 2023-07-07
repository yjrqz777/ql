import requests
import time

url = 'http://localhost:1338/backend-api/v2/conversation'
data = {"conversation_id": "d0b32d68-a841-4f9a-b7d4-1892ab5390a", "action": "_ask", "model": "gpt-3.5-turbo",
        "jailbreak": "default", "meta": {"id": "7252647883766641012",
                                         "content": {"conversation": '[]', "internet_access": "false",
                                                     "content_type": "text",
                                                     "parts": [{"content": "1", "role": "user"}]}}}
headers = {
    'Accept': 'text/event-stream',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '300',
    'Content-Type': 'application/json',
    'Dnt': '1',
    'Host': 'localhost:1338',
    'Origin': 'http://localhost:1338',
    'Referer': 'http://localhost:1338/chat/',
    'Sec-Ch-Ua': f'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}

if __name__ == '__main__':
    print("1")
    response = requests.post(url, headers=headers)
    print(response, end='\n')
