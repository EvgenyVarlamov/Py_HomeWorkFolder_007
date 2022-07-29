def log(data, stat):
    if stat == 'write_1':
        path = 'Phonebook\logs_1.txt'
    elif stat == 'write_4':
        path = 'Phonebook\logs_2.txt'
    with open(path, 'a') as file:
        file.write(data + '\n\n')


def read_file(stat):
    if stat == 'read_1':
        path = 'Phonebook\logs_1.txt'
    elif stat == 'read_4':
        path = 'Phonebook\logs_2.txt'
    with open(path, 'r') as file:
        return file.read()
