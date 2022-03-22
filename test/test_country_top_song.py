def test_get_filename_should_return_outfile_name(country_top_song, output_filename):
    assert country_top_song.get_filename() == output_filename


def test_count_frequency_of_songs_by_country_should_return_songs_counts_as_by_country(country_top_song, input_file):
    expected_dict = {'NP': {'101': 1, '102': 1}}
    with open(input_file) as file:
        country_top_song.count_frequency_of_songs_by_country(file)
        assert country_top_song.country_songs == expected_dict


def test_filter_top_n_songs_should_filter_songs_as_specified_in_number(country_top_song):
    result = country_top_song.filter_top_n_songs(count_dict={'NP': {'101': 1, '102': 1, '103': 10}})
    assert result[0] == "NP|103:10\n"
