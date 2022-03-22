import pytest

import processor


@pytest.fixture
def content():
    return "101|201|NP\n102|201|NP"


@pytest.fixture
def filename():
    return "listen-2022-03-20.log"


@pytest.fixture
def output_filename():
    return "country_top50_2022-03-20.txt"


@pytest.fixture
def input_file(tmp_path, filename, content):
    directory = tmp_path / 'input'
    directory.mkdir()
    file = directory / filename
    file.write_text(content)
    return file


def test_sort_by_value_should_sort_dict_in_reverse_order():
    test_dict = {'1': 10, '2': 21}
    actual_dict = processor.sort_by_value(test_dict)
    expected_dict = {'2': 21, '1': 10}
    assert actual_dict == expected_dict


def test_get_filename_should_generate_output_filename():
    input_file_name = "listen-2022-03-20.log"
    actual_output_filename = processor.get_filename(input_file_name)
    expected_filename = "country_top50_2022-03-20.txt"
    assert actual_output_filename == expected_filename


def test_count_frequency_of_songs_by_country_should_return_songs_counts_as_by_country(input_file):
    expected_dict = {'NP': {'101': 1, '102': 1}}
    with open(input_file) as file:
        actual_dict = processor.count_frequency_of_songs_by_country(file)
        assert actual_dict == expected_dict


def test_filter_top_n_songs_should_filter_songs_as_specified_in_number():
    result = processor.filter_top_n_songs(n=1, count_dict={'NP': {'101': 1, '102': 1, '103': 10}})
    assert result[0] == "NP|103:10\n"


@pytest.mark.usefixtures('filename')
def test_save_should_write_to_file_in_output_path_directory(tmp_path, filename, output_filename):
    directory = tmp_path / 'output'
    directory.mkdir()
    processor.save(values=["NP|103:10\n"],
                   file_name=filename,
                   output_path=directory)
    with open(directory / output_filename, "r") as file:
        assert file.readlines()[0] == "NP|103:10\n"
