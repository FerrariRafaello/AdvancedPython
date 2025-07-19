from collections import Counter
from typing import Dict, List

class DictAnalyzer:
    """
    Class for analyzing dictionary keys and their relationships.
    """
    def __init__(self, dict1: Dict, dict2: Dict):
        self.dict1 = dict1
        self.dict2 = dict2

    def common_keys(self):
        return self.dict1.keys() & self.dict2.keys()
    
    def keys_only_in_first(self):
        return self.dict1.keys() - self.dict2.keys()
    
    def keys_different_in_both(self):
        return self.dict1.keys() ^ self.dict2.keys()
    
    def all_keys(self):
        return self.dict1.keys() | self.dict2.keys()

    def display(self):
        print(f"Dict1 keys: {set(self.dict1.keys())}")
        print(f"Dict2 keys: {set(self.dict2.keys())}")
        print(f"Common keys: {self.common_keys()}")
        print(f"Keys only in dict1: {self.keys_only_in_first()}")
        print(f"Keys different in both: {self.keys_different_in_both()}")
        print(f"All keys combined: {self.all_keys()}")

class CounterAnalyzer:
    """
    Class for working with collections.COunter objects and their arithmetic.
    """

    def __init__(self, sequence: List):
        self.counter = Counter(sequence)

    def most_common(self, n: int):
        return self.counter.most_common(n)
    
    @staticmethod
    def combine_counters(counter_a: Counter, counter_b: Counter):
        return counter_a + counter_b
    
    def display(self):
        print(f"Counter elements: {self.counter}")


def main():
    d1 = {"marcos": 18, "joão": 30, "maria": 25}
    d2 = {"jose": 10, "marcos": 25, "joao": 19}
    dict_analyzer = DictAnalyzer(d1,d2)
    dict_analyzer.display()

    words = ["ola", "oi", "oi", "ola", "sera", "talvez", "quase", "talvez", "ola", "sei"]
    ca = CounterAnalyzer(words)
    ca.display()
    print("Top 2 most common words:", ca.most_common(2))
    print("Top 3 most common words:", ca.most_common(3))

    a = Counter([1,1,2,2,3,4,4,5,6,])
    b = Counter([2,2,1,3,5,6,7])
    print("Counter A:", a)
    print("Counter B:", b)
    combined = CounterAnalyzer.combine_counters(a, b)
    print("Combined Counter:", combined)

if __name__ == "__main__":
    main()