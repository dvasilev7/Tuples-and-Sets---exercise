phonebook = {}

contact = input()
while not contact.isnumeric():
    name, number = tuple(contact.split("-"))
    phonebook[name] = number
    contact = input()

n = int(contact)
for i in range(n):
    name = input()
    if name in phonebook:
        number = phonebook[name]
        print(f"{name} -> {number}")
    else:
        print(f"Contact {name} does not exist.")