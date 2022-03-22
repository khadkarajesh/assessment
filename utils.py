def sort_by_value(data: dict, reverse: bool = True) -> dict:
    return {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=reverse)}
