import pytest

from country_top_song import CountryTopSong
from user_top_song import UserTopSong


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
def user_output_filename():
    return "user_top50_2022-03-20.txt"


@pytest.fixture
def input_file(tmp_path, filename, content):
    directory = tmp_path / 'input'
    directory.mkdir()
    file = directory / filename
    file.write_text(content)
    return file


@pytest.fixture
def data_path(tmp_path):
    return tmp_path / "data"


@pytest.fixture
def output_path(data_path):
    return data_path / 'output'


@pytest.fixture
def input_file_name():
    return "listen-2022-03-20.log"


@pytest.fixture
def country_top_song(data_path, output_path, input_file_name):
    return CountryTopSong(n=1,
                          data_path=data_path,
                          output_path=output_path,
                          input_file=input_file_name)


@pytest.fixture
def user_top_song(data_path, output_path, input_file_name):
    return UserTopSong(n=1,
                       data_path=data_path,
                       output_path=output_path,
                       input_file=input_file_name)
