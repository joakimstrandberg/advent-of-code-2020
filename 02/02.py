file = open('input.txt', 'r')
l = file.readlines()
l = [ line.strip() for line in l]

num_valid = 0
for line in l:
    splt = line.split()
    #get fr and to
    fr = int(splt[0].split('-')[0])
    to = int(splt[0].split('-')[1])
    #get ch
    ch = splt[1][0]
    #get p
    p = splt[2]
    ctr = 0
    for i in p:
        if ch == i:
            ctr += 1
    if ctr >= fr and ctr <= to:
        num_valid += 1
print(num_valid)

# part 2
num_valid = 0
for line in l:
    splt = line.split()
    #get fr and to
    fr = int(splt[0].split('-')[0])-1
    to = int(splt[0].split('-')[1])-1
    #get ch
    ch = splt[1][0]
    #get p
    p = splt[2]
    b = False
    if ((ch==p[fr]) != (ch==p[to])):
        num_valid += 1
        b=True
    print(p[fr],p[to],ch,p,b)
print(num_valid)
