ans_pt1 = 0
ans_pt2 = 0
with open('input.txt', 'r') as f:
    for line in f:
        range1, range2 = line.strip().split(',')
        range1_start, range1_end = map(int, range1.split('-'))
        range2_start, range2_end = map(int, range2.split('-'))
        if range1_start <= range2_start <= range1_end and range1_start <= range2_end <= range1_end or\
                range2_start <= range1_start <= range2_end and range2_start <= range1_end <= range2_end:
            ans_pt1 += 1

        if range1_start <= range2_start <= range1_end or range2_start <= range1_start <= range2_end:
            ans_pt2 += 1

print(ans_pt1)
print(ans_pt2)
