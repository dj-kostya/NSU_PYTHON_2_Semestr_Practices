import json
import os
from pprint import pprint
INPUT_FILE = '4_knapsack.json'


def load_tests() -> list:
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f'Not found {INPUT_FILE}')
    with open(INPUT_FILE, 'r') as f:
        return json.load(f)


def knapsack(max_weight: int, items: list):
    max_len = len(items)

    def get_weight(bag: list) -> int:
        return sum([item['weight'] for item in bag])

    def get_price(bag: list) -> int:
        return sum([item['cost'] for item in bag])

    def try_item(idx: int, picked_items: list) -> list:
        if idx >= max_len:
            return picked_items
        exclude_bag = try_item(idx + 1, picked_items.copy())
        current_weight = get_weight(picked_items)
        include_bag: list = []
        if items[idx]['weight'] + current_weight <= max_weight:
            picked_items.append(items[idx])
            include_bag = try_item(idx + 1, picked_items.copy())
        return include_bag if include_bag and get_weight(include_bag) >= get_weight(exclude_bag) else exclude_bag

    result_bag = try_item(0, [])
    return {
        "capacity": len(result_bag),
        "items": result_bag,
        "weight": get_weight(result_bag),
        "value": get_price(result_bag)
    }


if __name__ == '__main__':
    tests = load_tests()
    for test_id, test in enumerate(tests):
        print(f'Test #{test_id}\nInput:')
        pprint(test)
        print('Output:')
        pprint(knapsack(test["max_weight"], test["items"]))
