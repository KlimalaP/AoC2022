alphabet_higher_case = {chr(i+64): i + 26 for i in range(1, 27)}
alphabet_lower_case = {chr(i+96): i for i in range(1, 27)}
arr = []
score = 0

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

for i in range(0, len(arr), 3):
    first, second, third = arr[i], arr[i+1], arr[i+2]
    common_item = list(set(first).intersection(second).intersection(third))[0]
    if common_item.islower():
        score = score + alphabet_lower_case.get(common_item)
    else:
        score = score + alphabet_higher_case.get(common_item)

print(score)


