n = int(input())

unique_el = set()

for i in range(n):
    elements = set(input().split())
    unique_el = unique_el.union(elements)

[print(element) for element in unique_el]