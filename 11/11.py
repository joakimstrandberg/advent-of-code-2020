file = open('input.txt', 'r')
l = file.read().splitlines()
#pad input since im lazy
pad = ''.join(['p' for i in range(0,len(l[0])) ])
l.insert(0,pad)
l.append(pad)

for i in range(0,len(l)):
    l[i] = "p" + l[i] + "p"

def pr(l):
    for i in range(0,len(l)):
        print(l[i])
    print('')

tmp_l = l.copy()
has_changed = True
while has_changed:
    has_changed = False
    for i in range(1,len(l)-1):
        for j in range(1,len(l[i])-1):
            adj_e = 0
            adj_o = 0
            #check over
            adj_e += l[i-1][j-1:j+2].count("L")
            adj_o += l[i-1][j-1:j+2].count("#")
            #check under
            adj_e += l[i+1][j-1:j+2].count("L")
            adj_o += l[i+1][j-1:j+2].count("#")
            #check left
            adj_e += l[i][j-1].count("L")
            adj_o += l[i][j-1].count("#")
            #check right
            adj_e += l[i][j+1].count("L")
            adj_o += l[i][j+1].count("#")

            #print(i,j)
            if l[i][j] == 'L':
                if adj_o ==0:
                    temp = list(tmp_l[i])
                    temp[j] = '#'
                    tmp_l[i] = ''.join(temp)
                    has_changed = True
            elif l[i][j] == '#':
                if adj_o >=4:
                    temp = list(tmp_l[i])
                    temp[j] = 'L'
                    tmp_l[i] = ''.join(temp)
                    has_changed = True
    l = tmp_l.copy()
    pr(l)

#count occupied
tot_o = 0
for i in range(1,len(l)-1):
    tot_o += l[i].count("#")
print(tot_o)

#Part 2
file = open('input.txt', 'r')
l = file.read().splitlines()
#pad input since im lazy
pad = ''.join(['p' for i in range(0,len(l[0])) ])
l.insert(0,pad)
l.append(pad)

for i in range(0,len(l)):
    l[i] = "p" + l[i] + "p"

def pr(l):
    for i in range(0,len(l)):
        print(l[i])
    print('')

tmp_l = l.copy()
has_changed = True
while has_changed:
    has_changed = False
    for i in range(1,len(l)-1):
        for j in range(1,len(l[i])-1):
            adj_e = 0
            adj_o = 0
            #check under
            for k in range(i+1,len(l)):
                tmp = l[k][j]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            #check over
            for k in range(i-1,0,-1):
                tmp = l[k][j]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            #check left
            for k in range(j-1,0,-1):
                tmp = l[i][k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break

            #check right
            for k in range(j+1,len(l[i])):
                tmp = l[i][k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            #check up diag left
            r = min(i,j)
            for k in range(1,r):
                tmp = l[i-k][j-k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            #check up diag right
            r = min(i,len(l[i])-j)
            for k in range(1,r):
                tmp = l[i-k][j+k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            #check down diag left
            r = min(len(l)-i,j)
            for k in range(1,r):
                tmp = l[i+k][j-k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break
            # check down diag right
            r = min(len(l)-i,len(l[i])-j)
            for k in range(1,r):
                tmp = l[i+k][j+k]
                if tmp == "#":
                    adj_o +=1
                    break
                elif tmp == "L":
                    adj_e +=1
                    break

            #print(i,j)
            if l[i][j] == 'L':
                if adj_o ==0:
                    temp = list(tmp_l[i])
                    temp[j] = '#'
                    tmp_l[i] = ''.join(temp)
                    has_changed = True
            elif l[i][j] == '#':
                if adj_o >=5:
                    temp = list(tmp_l[i])
                    temp[j] = 'L'
                    tmp_l[i] = ''.join(temp)
                    has_changed = True
    l = tmp_l.copy()
    pr(l)
#count occupied
tot_o = 0
for i in range(1,len(l)-1):
    tot_o += l[i].count("#")
print(tot_o)
