symbols = tuple(input())

symbols_and_occurrences = {}

for s in symbols:
    if s not in symbols_and_occurrences:
        symbols_and_occurrences[s] = 0
    symbols_and_occurrences[s] += 1

[print(f"{key}: {value} time/s") for key, value in sorted(symbols_and_occurrences.items(), key=lambda x: x[0])]