import re

arr = []
score = 0
alphabet_higher_case = {chr(i+64): i + 26 for i in range(1, 27)}
alphabet_lower_case = {chr(i+96): i for i in range(1, 27)}

with open('input.txt', 'r') as f:
    for line in f:
        lhs = line[:len(line)//2]
        rhs = line[len(line)//2:]
        for letter in lhs:
            pattern = re.compile(letter)
            match = pattern.search(rhs)
            if match:
                arr.append(match.group())
                break

for i in arr:
    if i.islower():
        score = score + alphabet_lower_case.get(i)
    else:
        score = score + alphabet_higher_case.get(i)

print(score)
