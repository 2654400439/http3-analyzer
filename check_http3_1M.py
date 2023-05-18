import http3
import csv
import numpy as np




# r = http3.get('https://www.a-msedge.net')
# print(r)
# try:
#     r = http3.get('https://www.wix.com')
# except KeyError:
#     print('not support')
# else:
#     print('support')


# 一些报错信息
# except http3.exceptions.ConnectTimeout:
#     print(data[i], 'timeout')
# except http3.exceptions.RedirectLoop:
#     print(data[i], 'RedirectLoop')
# except http3.exceptions.ReadTimeout:
#     print(data[i], 'ReadTimeout')
# except KeyError:
#     print(data[i], 'not support')
# except socket.gaierror:
#     print(data[i], 'socket error')
# except ConnectionRefusedError:
#     print(data[i], 'refused by source')

# headers = {'Accept': '*/*',
#             'Accept-Language': 'en-US,en;q=0.8',
#             'Cache-Control': 'max-age=0',
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
#             'Connection': 'keep-alive',
#             'Referer': 'http://www.baidu.com/'
#             }
#
#
# with open("D:/文件信工所/信工所/学习记录_调研/调研_互联网域名体系联动实施方案/top-1m.csv/top-1m.csv", 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     data = [row for row in reader]
# data = np.array(data)
# data = data[:, 1]
# add_str = 'https://www.'
#
# data = [add_str + item for item in data]
#
# for i in range(100):
#     try:
#         r = http3.get(data[i], headers = headers)
#     except Exception as e:
#         print(f"发生了错误：{str(e)}")
#     else:
#         print(data[i], 'support')
import asyncio
import aiohttp

# # 原始版
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


async def fetch(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            if 'alt-svc' in response.headers:
                return 'support'
            else:
                return 'not support'
    except Exception as e:
        return 'timeout'


async def main():
    urls = ['https://www.wix.com', 'https://www.google.com', 'https://www.github.com', 'https://www.facebook.com']
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())



