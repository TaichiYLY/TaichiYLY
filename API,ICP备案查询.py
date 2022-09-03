"""
API, ICP备案查询

Verion: 0.1
Author: Taichi

"""
import requests

def html_get(url,params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    params = {
        'url': params
    }
    data = requests.get(url=url, headers=headers,params=params)
    data.encoding = 'utf-8'
    return data.json()


if __name__ == '__main__':
    url = 'https://v.api.aa1.cn/api/icp/index.php?url=qq.com'
    print(html_get(url,'bilibili.com'))
