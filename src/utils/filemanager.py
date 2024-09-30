from src.utils import timer
import time
import os


# open()函数: 用来打开一个文件，返回一个文件对象。
# 模式参数: 指定打开文件的模式，常用的有：
# 'r': 以只读方式打开 (默认)
# 'w': 以写方式打开，若文件存在则覆盖，不存在则创建
# 'a': 以追加模式打开，若文件存在则在末尾追加数据，不存在则创建
# 'x': 创建新文件，如果文件已存在则报错
# 'b': 以二进制模式打开 (常用于处理图片、音频等非文本文件)
# '+': 打开文件用于读写


def write_today_log_with(data, mode="w"):
    with open(timer.get_today_date_str() + ".txt", mode) as f:
        for key, value in data.items():
            f.write(f"{key} {value}\n")


def read_data_from(file_name):
    data: dict[str, int] = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                key, value_str = line.strip().split(' ')
                data[key] = int(value_str)
    return data


def run_interval_with(func, *args, time_interval=300):
    while True:
        func(args[0], args[1])
        time.sleep(time_interval)
