import pickle

# Example dictionary to serialize
users = {
    '1234-5': 'Alice',
    '1235-6': 'Bob',
    '1236-7': 'Charlie',
}

# Save the dictionary to a binary file using pickle
with open('data.dat', 'wb') as file:
    pickle.dump(users, file)
print(f'The collection {users} was saved to "data.dat".')

# Load the dictionary back from the file
with open('data.dat', 'rb') as file:
    loaded_users = pickle.load(file)
print('Reading data from "data.dat":')
print(f'Users: {loaded_users}')
print(f'User with key "1234-5": {loaded_users["1234-5"]}')

print('\n')

# Reading a text file line by line without using 'with' (not recommended)
file = open('contacts.txt', 'r+')
print('Content of "contacts.txt":')
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')
file.close()

print('\n')

# Reading a text file line by line using 'with' (recommended)
print('Content of "contacts.txt" (using with):')
with open('contacts.txt', 'r+') as file:
    for line in file:
        print(line, end='')
