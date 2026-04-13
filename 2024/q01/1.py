from collections import Counter
with open('input.txt')as f:
    data = f.read()
counts = Counter(data)
print(counts['B'] + counts['C'] * 3)