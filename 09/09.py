file = open('input.txt', 'r')
l = file.read().splitlines()
l  = list(map(int, l))

for i in range(25,len(l)):
    preamble = l[i-25:i]
    next = l[i]
    correct = False
    for first in range(0,len(preamble)):
        for second in range(0,len(preamble)):
            s = preamble[first] + preamble[second]
            #print(sum)
            if first == second:
                break
            if s == next:
                correct = True
                break
        if correct:
            break
    if not correct:
        break
print(next)
#Part 2
invalid = next
correct = False
for n in range(2,len(l)):
    for i in range(n,len(l)):
        c_set = l[i-n:i]
        correct = False
        s = sum(c_set)
        if s == invalid:
            correct = True
            break
    if correct:
        break
c_set.sort()
print(c_set[0]+c_set[-1])
