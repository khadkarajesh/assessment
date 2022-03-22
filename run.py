import concurrent.futures
import datetime
import time
from pathlib import Path
from typing import List

from country_top_song import CountryTopSong

DATA_PATH = Path.cwd() / 'data'
INPUT_PATH = DATA_PATH / 'input'
OUTPUT_PATH = DATA_PATH / 'output'


def prepare_args(names: List[str]):
    return [[50, DATA_PATH, OUTPUT_PATH, name] for name in names]


def wrapper(p):
    return CountryTopSong(*p).discover()


if __name__ == "__main__":
    print("Job started....")
    print("Job in progress....")

    start_time = time.time()

    today = datetime.datetime.today()
    dates = [(today - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(1, 8)]
    file_names = [f"listen-{date}.log" for date in dates]

    results = prepare_args(names=file_names)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(wrapper, results)
    elapsed_time = time.time() - start_time

    print(f"Job completed. Elapsed time {round(elapsed_time, 2)} sec")
