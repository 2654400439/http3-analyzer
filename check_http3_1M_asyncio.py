import asyncio
import aiohttp
import numpy as np
import csv

# # 原始版
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


def load_data():
    with open("D:/文件信工所/信工所/学习记录_调研/调研_互联网域名体系联动实施方案/top-1m.csv/top-1m.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    data = np.array(data)
    data = data[:, 1]
    add_str = 'https://www.'

    data = [add_str + item for item in data]
    return data


async def fetch(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            if 'alt-svc' in response.headers:
                return url + ' support'
            else:
                return url + ' not support'
    except Exception as e:
        return 'timeout'


async def main():
    urls = load_data()[:100]
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