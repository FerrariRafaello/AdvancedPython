from typing import Iterable, Any

def to_set(sequence: Iterable[Any]):
    """
    Convert any iterable sequence into a set to remove duplicates.
    Accepts lists, tuples, strings, generators, etc.
    """
    return set(sequence)

def to_list_no_duplicates(sequence: Iterable[Any]):
    """
    Convert any iterable sequence into a list with duplicates removed.
    The order is not guaranteed because sets are unordered.
    """
    return list(set(sequence))


# Example:
duplicate_list = ['Alice', 'Bob', 'Carl', 'Bob', 'Alice', 'Carl']
print(f'Original list with duplicates: {duplicate_list}\n')

unique_set = to_set(duplicate_list)
print(f'Converted to set (duplicates removed): {unique_set}\n')

unique_list = to_list_no_duplicates(duplicate_list)
print(f'Converted back to list without duplicates: {unique_list}\n')

sample_tuple = ('apple', 'banana', 'apple', 'cherry')
print(f'Original tuple: {sample_tuple}\n')
print(f'Tuple converted to set: {to_set(sample_tuple)}\n')
print(f'Tuple converted to list without duplicates: {to_list_no_duplicates(sample_tuple)}\n')

sample_string = "banana"
print(f'Original string: {sample_string}\n')
print(f'String converted to set: {to_set(sample_string)}\n')
print(f'String converted to list without duplicates: {to_list_no_duplicates(sample_string)}')
