import time
import os
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'.E/777/{number}.txt' for number in range(1, 5)]


def linear_read():
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    end_time = time.monotonic()
    print(f"Линейный вызов занял: {end_time - start_time} секунд")


def multiprocess_read():
    start_time = time.monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.monotonic()
    print(f"Многопроцессный вызов занял: {end_time - start_time} секунд")


if __name__ == '__main__':

    linear_read()

