def test_get_filename_should_return_outfile_name(user_top_song, user_output_filename):
    assert user_top_song.get_filename() == user_output_filename


def test_count_frequency_of_songs_by_user_should_count_songs_played_by_user(user_top_song, input_file):
    expected_dict = {'201': {'101': 1, '102': 1}}
    with open(input_file) as file:
        user_top_song.count_frequency_of_songs_by_user(file)
        assert user_top_song.user_songs == expected_dict


def test_filter_top_n_songs_should_filter_songs_as_specified_in_number(user_top_song):
    result = user_top_song.filter_top_n_songs(count_dict={'201': {'101': 1, '102': 1, '103': 10}})
    assert result[0] == "201|103:10\n"
