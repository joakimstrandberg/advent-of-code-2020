file = open('input.txt', 'r')
l = file.read().splitlines()
l  = list(map(int, l))

l.sort()
diffs = [l[0]]
diffs.extend([l[i+1] - l[i] for i in range(0,len(l)-1)])
diffs.extend([3])
three = diffs.count(3)
one = diffs.count(1)

print(set(diffs))
print(three*one)
#Part 2

def rec(remaining_list,sel):
    #find selectable
    diff = 0
    tot = 0
    for i,item in enumerate(remaining_list):
        if diff > 2:
            break
        diff+=item
        new_sel = sel.copy()
        for j in range(0,i):
            new_sel.append(0)
        new_sel.append(item)
        tot += rec(remaining_list[i+1:],new_sel)
    if remaining_list == []:
        print(sel)
        tot = 1
    return tot

one_list = []
comb = 1
for i in diffs:
    if i == 3:
        comb *= rec(one_list,[])
        one_list = []
    one_list.append(i)

print(comb)
