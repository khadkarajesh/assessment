import argparse
import concurrent.futures
import datetime
import time
from pathlib import Path
from typing import List

from song.country_top_song import CountryTopSong
from song.user_top_song import UserTopSong

DATA_PATH = Path.cwd() / 'data'
INPUT_PATH = DATA_PATH / 'input'
OUTPUT_PATH = DATA_PATH / 'output'


def prepare_args(names: List[str]):
    return [[50, DATA_PATH, OUTPUT_PATH, name] for name in names]


def country_song_wrapper(p):
    return CountryTopSong(*p).discover()


def user_song_wrapper(p):
    return UserTopSong(*p).discover()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--type", default="country_top_50_song", help="generate type of report")
    args = parser.parse_args()
    config = vars(args)

    action_type = config.get('type')

    print("Job started....")
    print("Job in progress....")

    start_time = time.time()

    today = datetime.datetime.today()
    dates = [(today - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(1, 8)]
    file_names = [f"listen-{date}.log" for date in dates]

    results = prepare_args(names=file_names)
    if action_type == "country_top_50_song":
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(country_song_wrapper, results)
    else:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(user_song_wrapper, results)
    elapsed_time = time.time() - start_time

    print(f"Job completed. Elapsed time {round(elapsed_time, 2)} sec")
