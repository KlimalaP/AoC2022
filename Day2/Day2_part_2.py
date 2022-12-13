arr = []
score = 0

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip().split(" "))

winners = {'A': 'Z',
           'B': 'X',
           'C': 'Y'}

losers = {'A': 'Y',
          'B': 'Z',
          'C': 'X'}

points = {'X': 1,
          'A': 1,
          'Y': 2,
          'B': 2,
          'Z': 3,
          'C': 3}

for battle in arr:
    if battle[1] == 'Y':
        score = score + 3 + points[battle[0]]
    elif battle[1] == 'X':
        score = score + points[winners[battle[0]]]
    else:
        score = score + 6 + points[losers[battle[0]]]

print(score)