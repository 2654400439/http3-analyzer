import multiprocessing
import http3
import csv
import numpy as np
import os
import tqdm
import random

headers = {'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'http://www.baidu.com/'
            }


def load_data():
    with open("D:/文件信工所/信工所/学习记录_调研/调研_互联网域名体系联动实施方案/top-1m.csv/top-1m.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    data = np.array(data)
    data = data[:, 1]
    add_str = 'https://www.'

    data = [add_str + item for item in data]
    return data


def process_task(url):
    with open('check_http3_result_' + str(os.getpid()) + '.csv', 'a', newline='') as csvfile:
        try:
            r = http3.get(url, headers=headers)
        except Exception as e:
            result = [url.split('www.')[1], "error"]
        else:
            try:
                result = [url.split('www.')[1], "support"] if str(r.headers['alt-svc']).find('h3') != -1 else [url.split('www.')[1], "not support"]
            except KeyError:
                result = [url.split('www.')[1], "not support"]
        writer = csv.writer(csvfile)
        writer.writerow(result)


if __name__ == "__main__":
    tasks = load_data()
    random.shuffle(tasks)

    pool = multiprocessing.Pool(processes=10)

    # pool.map(process_task, tasks)
    with tqdm.tqdm(total=len(tasks)) as pbar:
        for _ in pool.imap(process_task, tasks):
            pbar.update(1)

    pool.close()
    pool.join()
