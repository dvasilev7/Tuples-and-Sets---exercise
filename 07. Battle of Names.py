n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    value = 0
    for symbol in name:
        value += int(ord(symbol))
    value //= i
    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

if sum(odd_set) == sum(even_set):
    print(", ".join([str(num) for num in odd_set.union(even_set)]))
elif sum(odd_set) > sum(even_set):
    print(", ".join([str(number) for number in odd_set.difference(even_set)]))
elif sum(odd_set) < sum(even_set):
    print(", ".join([str(number) for number in even_set.symmetric_difference(odd_set)]))