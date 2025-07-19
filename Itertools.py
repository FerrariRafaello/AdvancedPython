import itertools

for p in itertools.permutations([1,2,3]):
    print("".join(map(str, p)))

people_ages = {"marcos": 28, "joao": 19, "maria": 25}
print("People and ages:", people_ages)

print("Marcos age:", people_ages["marcos"])

print("Joao age:", people_ages["joao"])

if people_ages.get("blabla") is not None:
    print("Key exists")
else:
    print("Key does not exists")

l1 = [1,2,3]
l2 = [4,5,6]
l3 = ["Python", "PHP", "Go"]

combined = itertools.chain(l1,l2,l3)
print("Combined lists:", list(combined))