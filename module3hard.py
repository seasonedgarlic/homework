data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    sums = 0
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            sums += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            sums += calculate_structure_sum(key)
            sums += calculate_structure_sum(value)
    return sums


result = calculate_structure_sum(data_structure)
print(result)