import pytest

from utils import sort_by_value


def test_sort_by_value_should_sort_dict_in_reverse_order():
    test_dict = {'1': 10, '2': 21}
    actual_dict = sort_by_value(test_dict)
    expected_dict = {'2': 21, '1': 10}
    assert actual_dict == expected_dict

# @pytest.mark.usefixtures('filename')
# def test_save_should_write_to_file_in_output_path_directory(tmp_path, filename, output_filename):
#     directory = tmp_path / 'output'
#     directory.mkdir()
#     processor.save(values=["NP|103:10\n"],
#                    file_name=filename,
#                    output_path=directory)
#     with open(directory / output_filename, "r") as file:
#         assert file.readlines()[0] == "NP|103:10\n"
