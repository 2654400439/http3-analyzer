# import asyncio
# import time
#
#
# async def wait(t):
#     await asyncio.sleep(t)
#
#
# async def main():
#     # task1 = asyncio.create_task(wait(1))
#     # task2 = asyncio.create_task(wait(2))
#
#     print('start at:', time.strftime('%X'))
#     await asyncio.gather(wait(1), wait(2))
#     print('end at:', time.strftime('%X'))
#
# asyncio.run(main())

import http3
import asyncio
import csv
import numpy as np
import requests
import time


def load_url(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = np.array([row for row in reader])
    return data[:, 1]


async def check_http3(url):
    try:
        _ = requests.get(url, timeout=4)
    except Exception:
        return 0
    else:
        return 1


async def main():
    start = time.time()
    result = await asyncio.gather(check_http3(data[0]), check_http3(data[0]), check_http3(data[0]))
    end = time.time()

    print(result, end-start)


data = load_url("D:/文件信工所/信工所/学习记录_调研/调研_互联网域名体系联动实施方案/top-1m.csv/top-1m.csv")
add_str = 'https://www.'
data = [add_str + item for item in data]

asyncio.run(main())







