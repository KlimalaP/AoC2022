arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

print(arr)

calories_arr = []
sum = 0

for calories in arr:
    if calories != '':
        sum += int(calories)
    else:
        calories_arr.append(sum)
        sum = 0

max_calories = max(calories_arr)
print(max_calories)

#Pt. 2

calories_arr = sorted(calories_arr, reverse=True)
print(calories_arr[0] + calories_arr[1] + calories_arr[2])
