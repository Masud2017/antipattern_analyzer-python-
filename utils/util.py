def divide_dict_into_batches(batch_size: int = 3, data_dict: dict = {}) -> list[dict]:
    items = list(data_dict.items())
    return [dict(items[i:i + batch_size]) for i in range(0, len(items), batch_size)]
