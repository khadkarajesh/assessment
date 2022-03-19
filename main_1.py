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
    file_output = []
    for country in mapped_data.keys():
        songs_dict = mapped_data.get(country)
        sorted_songs_dict = {k: v for k, v in sorted(songs_dict.items(), key=lambda item: item[1], reverse=True)}
        formatted_line = f"{country}|"
        song_txt = ""
        top_songs_keys = list(sorted_songs_dict.keys())[0:50]
        for song in top_songs_keys:
            song_txt = song_txt + f"{song}:{sorted_songs_dict[song]},"
        file_output.append(f"{country}|{song_txt.rstrip(',')}\n")
    with open("result.txt", "w") as result_file:
        result_file.writelines(file_output)
