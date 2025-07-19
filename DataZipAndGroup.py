from typing import List, Tuple, Dict, Any
from operator import itemgetter
from itertools import groupby

def zip_lists(*lists: List[Any]):
    """
    Zip multiple lists into a list of tuples.
    Stops at the shortest list length.
    """
    return list(zip(*lists))

def group_by_key(data: List[Tuple[str, int]], key_index: int = 0):
    """
    Group a list of tuples by the element at key_index,
    returning a dict where each key maps to a sorted list of corresponding values.
    """
    data_sorted = sorted(data, key = itemgetter(key_index))

    grouped = {
        key: sorted(map(itemgetter(1), group))
        for key, group in groupby(data_sorted, key=itemgetter(key_index))
    }
    return grouped

if __name__ == "__main__":
    zipped1 = zip_lists([1,2,3], [4,5,6])
    print("Zipped pairs:", zipped1)

    zipped2 = zip_lists([1,2,3], [4,5,6], [7,8,9,])
    print("Zipped triples:", zipped2)

    data = [
        ("marcos", 28),
        ("pedro", 19),
        ("joao", 20),
        ("marcos", 20),
        ("joao", 18),
        ("marcos", 30),
    ]

    grouped_data = group_by_key(data)
    print("Grouped data:", grouped_data)