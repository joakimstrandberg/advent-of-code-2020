file = open('input.txt', 'r')
l = file.read().splitlines()
rules = []

#first 10
for i,line in enumerate(l[:10]):
    d1 = line.split()[2]
    temp1 = int(d1.split("-")[0])
    temp2 = int(d1.split("-")[1])
    first = [temp1,temp2]
    d2 = line.split()[4]
    temp1 = int(d2.split("-")[0])
    temp2 = int(d2.split("-")[1])
    sec = [temp1,temp2]
    rules.append([first,sec])
#11-20
for i,line in enumerate(l[10:20]):
    if i > 9:
        break
    d1 = line.split()[1]
    first = [int(d1.split("-")[0]),int(d1.split("-")[1])]
    d2 = line.split()[3]
    sec = [int(d2.split("-")[0]),int(d2.split("-")[1])]
    rules.append([first,sec])

#my tickets
tickets = l[22].strip().split(",")
tickets = list(map(int, tickets))
rule_set = set()
for j in rules:
    for k in j:
        for m in range(k[0],k[1]):
            rule_set.add(m)

invalid_sum = 0
for line in l[25:]:
    nearby = line.strip().split(",")
    nearby = list(map(int, nearby))
    for i in nearby:
        if i not in rule_set:
            invalid_sum += i
print(invalid_sum)

#Part 2
file = open('input.txt', 'r')
l = file.read().splitlines()
rules = []

#first 10
for i,line in enumerate(l[:10]):
    d1 = line.split()[2]
    temp1 = int(d1.split("-")[0])
    temp2 = int(d1.split("-")[1])
    tempset = set()

    for m in range(temp1,temp2+1):
        tempset.add(m)
    d2 = line.split()[4]
    temp1 = int(d2.split("-")[0])
    temp2 = int(d2.split("-")[1])
    for m in range(temp1,temp2+1):
        tempset.add(m)
    rules.append(tempset)
#11-20
for i,line in enumerate(l[10:20]):
    d1 = line.split()[1]
    first = [int(d1.split("-")[0]),int(d1.split("-")[1])]
    tempset = set()
    for m in range(first[0],first[1]+1):
        tempset.add(m)
    d2 = line.split()[3]
    sec = [int(d2.split("-")[0]),int(d2.split("-")[1])]
    for m in range(sec[0],sec[1]+1):
        tempset.add(m)
    rules.append(tempset)

#my tickets
tickets = l[22].strip().split(",")
tickets = list(map(int, tickets))
#print(rules)

invalid_tickets = set()
nearby_tickets = l[25:]
nearby_tickets = [list(map(int,i.strip().split(","))) for i in nearby_tickets]
#print(nearby_tickets)
in_rules = False
for line in nearby_tickets:
    #nearby = line.strip().split(",")
    #nearby = list(map(int, nearby))
    for i in line:
        in_rules = False
        for r in rules:
            if i in r:
                in_rules = True
        if not in_rules:
            invalid_tickets.add("".join([str(k)+"," for k in line]))

#print(invalid_tickets)
valid_tickets = [i for i in nearby_tickets if "".join([str(k)+"," for k in i]) not in invalid_tickets]
valid_tickets.append(tickets)
rule_dict = {}
invalid_rule = False
for r_idx, r in enumerate(rules):
    for i in range(0,len(valid_tickets[0])):
        invalid_rule = False
        for j in range(0,len(valid_tickets)):
            temp =  valid_tickets[j][i]
            if temp not in r:
                invalid_rule = True
                break
        if not invalid_rule:
            if r_idx in rule_dict.keys():
                temp = rule_dict[r_idx]
                temp.append(i)
                rule_dict[r_idx] = temp
            else:
                temp = []
                temp.append(i)
                rule_dict[r_idx] = temp
is_finished = False
while not is_finished:
    is_finished = True
    for key in rule_dict.keys():
        if len(rule_dict[key]) == 1:
            for k in rule_dict.keys():
                if k == key:
                    continue
                if rule_dict[key][0] in rule_dict[k]:
                    is_finished = False
                    temp = rule_dict[k]
                    temp.remove(rule_dict[key][0])

print(rule_dict)
mult = 1
for i in range(0,6):
    mult *= tickets[rule_dict[i][0]]
print(mult)
