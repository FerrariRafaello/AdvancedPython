from itertools import groupby
from operator import itemgetter
import math
from typing import List, Dict, Any

def group_data_by_date(records: List[Dict[str, Any]], key_field: str = "data"):
    """
    Groups and prints records by a specific key (default is "data").

    Args:
        records: List of dictionaries containing data.
        key_field: The field by which to group the records.

    This function sorts the records by the key_field and then 
    groups them using itertools.groupby, printing each group.
    """
    # Sort by the key field to ensure groupby works correctly
    records.sort(key=itemgetter(key_field))

    for key_value, group_items in groupby(records, key=itemgetter(key_field)):
        print(f"Group: {key_value}")
        for item in group_items:
            print(f" {item}")

def filter_list(values: List[int]):
    """
    Demonstrates filtering of a list using list comprehensions.

    Args:
        values: List of integers.

    Prints:
        - Negative numbers
        - Positive numbers
        - Maximum value(s)
        - Minimum value(s)
        - Square roots of values > 1
    """
    print(f"Original list: {values}")

    negatives = [x for x in values if x < 0]
    print(f"Negative values: {negatives}")

    positivies = [x for x in values if x > 0]
    print(f"Positive values: {positivies}")

    max_values = [x for x in values if x == max(values)]
    print(f"Maximum value(s): {max_values}")

    min_values = [x for x in values if x == min(values)]
    print(f"Minimum value(s): {min_values}")

    sqrt_values = [math.sqrt(x) for x in values if x > 1] 
    print(f"Square roots of values > 1: {sqrt_values}")


if __name__ == "__main__":
    sample_records = [
        {"nome": "Marcos", "data": "27/12/1987"},
        {"nome": "Joao", "data": "18/11/1967"},
        {"nome": "Maria", "data": "27/12/1987"},
        {"nome": "Julia", "data": "18/11/1967"},
        {"nome": "Pedro", "data": "18/11/1967"},
    ]

    group_data_by_date(sample_records)

    sample_list = [10 ,-5, 20, 30, -40, 100]
    filter_list(sample_list)