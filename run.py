import datetime
from pathlib import Path
from typing import List
import concurrent.futures
import time

from processor import get_top_songs

DATA_PATH = Path.cwd() / 'data'
INPUT_PATH = DATA_PATH / 'input'
OUTPUT_PATH = DATA_PATH / 'output'


def prepare_args(names: List[str]):
    return [[50, DATA_PATH, OUTPUT_PATH, name] for name in names]


def wrapper(p):
    return get_top_songs(*p)


if __name__ == "__main__":
    print("Job started....")
    print("Job in progress....")

    start_time = time.time()

    today = datetime.datetime.today()
    dates = [(today - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(1, 8)]
    file_names = [f"listen-{date}.log" for date in dates]

    # results = prepare_args(names=file_names)
    #
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = executor.map(wrapper, results)
    # elapsed_time = time.time() - start_time
    #
    # print(f"Job completed. Elapsed time {round(elapsed_time, 2)} sec")

    get_top_songs(n=50, data_path=DATA_PATH, output_path=OUTPUT_PATH, input_file=file_names[3])
