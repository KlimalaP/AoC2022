arr = []
with open('input.txt', 'r') as f:
    for line in f:
        sub_s = line.strip().split(" ")
        for i, x in enumerate(sub_s):
            if x == 'A' or x == 'X':
                sub_s[i] = 'ROCK'
            elif x == 'B' or x == 'Y':
                sub_s[i] = 'PAPER'
            elif x == 'C' or x == 'Z':
                sub_s[i] = 'SCISSORS'

        arr.append(sub_s)


points = {'ROCK': 1,
          'PAPER': 2,
          'SCISSORS': 3}

winners = {'ROCK': 'SCISSORS',
           'SCISSORS': 'PAPER',
           'PAPER': 'ROCK'}

score = 0

for battle in arr:
    if battle[0] == battle[1]:
        score = score + 3 + points[battle[1]]
    elif battle[0] == winners[battle[1]]:
        score = score + 6 + points[battle[1]]
    else:
        score = score + points[battle[1]]

print(score)