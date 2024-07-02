def calculate_structure_sum(args):
    total_amount = 0
    for item in args:
        total_amount += get_item_value(item)

    return total_amount


def get_item_value(item):
    amount = 0
    if isinstance(item, str):
        amount = len(item)
    if isinstance(item, int):
        amount = item
    if isinstance(item, tuple):
        for single_item in item:
            amount += get_item_value(single_item)
    if isinstance(item, dict):
        for single_item in item.keys():
            amount += get_item_value(single_item)
        for single_item in item.values():
            amount += get_item_value(single_item)
    if isinstance(item, set):
        for single_item in item:
            amount += get_item_value(single_item)
    if isinstance(item, list):
        for single_item in item:
            amount += get_item_value(single_item)

    return amount


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
