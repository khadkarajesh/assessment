import re
from pathlib import Path

from song.country_top_song import LOG_FORMAT_REGEX
from song.top_song import TopSong
from utils import sort_by_value

OUTPUT_FILE_NAME_PREFIX = "user_top50_"


class UserTopSong(TopSong):
    def __init__(self, n: int,
                 data_path: Path,
                 output_path: Path,
                 input_file):
        super().__init__(n, data_path, output_path, input_file)

    def count_frequency(self, file):
        for line in file:
            pattern = re.compile(LOG_FORMAT_REGEX)
            if pattern.match(line):
                results = line.strip().split("|")
                user_id = results[1]
                song_id = results[0]
                if self.count_storage.get(user_id):
                    song_dict = self.count_storage[user_id]
                    if song_dict.get(song_id):
                        song_dict[song_id] += 1
                    else:
                        song_dict[song_id] = 1
                else:
                    self.count_storage[user_id] = {song_id: 1}

    def filter(self):
        for key in self.count_storage.keys():
            songs_dict = self.count_storage.get(key)
            sorted_songs_dict = sort_by_value(songs_dict)
            song_txt = ""
            top_songs_keys = list(sorted_songs_dict.keys())[0:self.n]
            for song in top_songs_keys:
                song_txt = song_txt + f"{song}:{sorted_songs_dict[song]},"
            self.result.append(f"{key}|{song_txt.rstrip(',')}\n")

    def get_output_file_prefix(self):
        return OUTPUT_FILE_NAME_PREFIX
