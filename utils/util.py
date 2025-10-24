def divide_list_into_batches(batch_size:int = 3, data_list:list = []) -> list[list]:
    return [data_list[i:i + batch_size] for i in range(0, len(data_list), batch_size)]
