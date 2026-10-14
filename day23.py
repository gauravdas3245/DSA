words = ["apple", "cat", "banana", "dog", "kiwi"]

groups = {}

for word in words:
    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)
