import re
from pathlib import Path
from typing import List

from logger import logger

LOG_FORMAT_REGEX = r"^[0-9]+\|[0-9]+\|[A-Z]{2}$"
OUTPUT_FILE_NAME_PREFIX = "country_top50_"


def get_song_by_country(file) -> dict:
    country_song_dict = {}
    for line in file:
        pattern = re.compile(LOG_FORMAT_REGEX)
        if pattern.match(line):
            line = line.strip()
            results = line.split("|")
            country = results[2]
            song_id = results[0]
            if country_song_dict.get(country):
                song_dict = country_song_dict[country]
                if song_dict.get(song_id):
                    song_dict[song_id] += 1
                else:
                    song_dict[song_id] = 1
            else:
                country_song_dict[country] = {song_id: 1}
    return country_song_dict


def generate_file(values: List[str], file_name: str, output_path: Path) -> None:
    with open(output_path / generate_file_name(file_name), "w") as result_file:
        result_file.writelines(values)


def generate_file_name(input_file_name: str) -> str:
    log_file_date = input_file_name[7:18]
    return f"{OUTPUT_FILE_NAME_PREFIX}{log_file_date}.txt"


def sort_by_value(data: dict, reverse: bool = True) -> dict:
    return {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=reverse)}


def extract_top_n_songs(n: int, count_dict: dict) -> List[str]:
    result = []
    for key in count_dict.keys():
        songs_dict = count_dict.get(key)
        sorted_songs_dict = sort_by_value(songs_dict)
        song_txt = ""
        top_songs_keys = list(sorted_songs_dict.keys())[0:n]
        for song in top_songs_keys:
            song_txt = song_txt + f"{song}:{sorted_songs_dict[song]},"
        result.append(f"{key}|{song_txt.rstrip(',')}\n")
    return result


def get_top_songs(n: int,
                  data_path: Path,
                  output_path: Path,
                  input_file) -> None:
    try:
        with open(data_path / 'input' / input_file) as f:
            data = get_song_by_country(f)
            top_n_songs = extract_top_n_songs(n=n, count_dict=data)
            generate_file(top_n_songs, input_file, output_path=output_path)
    except FileNotFoundError as e:
        logger.error(e)
