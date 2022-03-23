def sort_by_value(data: dict, reverse: bool = True) -> dict:
    """
    Sorts dictionary as per values in reverse order
    :param data: dictionary to sort
    :param reverse: default True
    :return: dictionary sorted in reverse order by values
    """
    return {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=reverse)}
