
file = open('input.txt', 'r')
l = file.read().splitlines()
sum_q= 0
q_set = set()
#to add the last group
l.append("")
for line in l:
    if line != "":
        for ch in line:
            q_set.add(ch)
    else:
        sum_q += len(q_set)
        q_set.clear()
print(sum_q)
###### part 2 ######
sum_q= 0
q_set_list = []
#to add the last group
l.append("")
for line in l:
    if line != "":
        q_set = set()
        for ch in line:
            q_set.add(ch)
        q_set_list.append(q_set)
    else:
        if len(q_set_list) > 0:
            intersection = q_set_list[0]
            for s in q_set_list[1:]:
                intersection = set.intersection(intersection, s)
            sum_q += len(intersection)
            q_set_list = []
print(sum_q)
