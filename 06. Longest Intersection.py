n = int(input())

longest_intersection = set()


for i in range(n):
    t = tuple(input().split("-"))
    f_start, f_end = [int(number) for number in t[0].split(",")]
    s_start, s_end = [int(number) for number in t[1].split(",")]
    f_set = set()
    s_set = set()
    for num in range(f_start, f_end + 1):
        f_set.add(num)
    for num in range(s_start, s_end + 1):
        s_set.add(num)
    intersection = f_set.intersection(s_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

longest_intersection = list(longest_intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")