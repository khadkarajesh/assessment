from utils import sort_by_value


def test_sort_by_value_should_sort_dict_in_reverse_order():
    test_dict = {'1': 10, '2': 21}
    actual_dict = sort_by_value(test_dict)
    expected_dict = {'2': 21, '1': 10}
    assert actual_dict == expected_dict
