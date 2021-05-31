numbers_list = input().split()
n = int(numbers_list[0])
m = int(numbers_list[1])

n_set = set()
m_set = set()

for i in range(n + m):
    number = input()
    if i < n:
        n_set.add(number)
    else:
        m_set.add(number)

[print(number) for number in n_set.intersection(m_set)]
