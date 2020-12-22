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

invalid_tickets = set()
nearby_tickets = l[25:]
for line in nearby_tickets:
    nearby = line.strip().split(",")
    nearby = list(map(int, nearby))
    for i in nearby:
        if i not in rule_set:
            invalid_tickets.add(i)

valid_tickets = [i for i in nearby_tickets if i not in invalid_tickets]

rule_dict = {}
for 
