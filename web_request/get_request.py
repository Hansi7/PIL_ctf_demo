import requests
import time


def save(txt):
    with open(str(time.time()) + '.html', 'w', encoding='utf8') as f:
        f.write(txt)


r = requests.session()

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept - Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
           'Connection': 'Keep-Alive',
           'Host': 'zhannei.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
params = {'wd': 'weather'}

response = r.get('https://baidu.com/s', params=params, headers=headers)
save(response.text)
print(response.text)
print(eval('1+1'))

response = r.post('http://baidu.com/', data={'wd': 'sdf'})
print(response.text)
save(response.text)
