import re

name_file = "sample_listen-2021-12-01_2Mlines.log"
LOG_FORMAT = r"^[0-9]+\|[0-9]+\|[A-Z]{2}$"
mapped_data = dict()
with open(name_file) as f:
    for line in f:
        pattern = re.compile(LOG_FORMAT)
        if pattern.match(line):
            line = line.strip()
            results = line.split("|")
            country = results[2]
            song_id = results[0]
            if mapped_data.get(country):
                song_dict = mapped_data[country]
                if song_dict.get(song_id):
                    song_dict[song_id] += 1
                else:
                    song_dict[song_id] = 1
            else:
                mapped_data[country] = {song_id: 1}
with open("result.json", "w") as file:
    file.write(mapped_data)
