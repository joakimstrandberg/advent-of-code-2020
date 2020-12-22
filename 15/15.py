file = open('input.txt', 'r')
l = file.read().strip().split(",")
l = list(map(int, l))
print(l)

mem = {}

for i,num in enumerate(l):
    mem[num] = [i+1]
    last_num = num
#last_num =16
k = len(l)+1
print(k)
while True:
    print(mem)
    if last_num in mem.keys():
        if len(mem[last_num]) == 2:
            last_num = mem[last_num][1] - mem[last_num][0]
            if last_num in mem.keys():
                temp = mem[last_num]
                temp.append(k)
                if len(temp) == 3:
                    temp.pop(0)
                mem[last_num] = temp
            else:
                mem[last_num] = [k]
        else:
            last_num = 0
            temp = mem[last_num]
            temp.append(k)
            if len(temp) ==3:
                temp.pop(0)
            mem[last_num] = temp
    else:
        last_num = 0
        temp = mem[last_num]
        temp.append(k)
        if len(temp) ==3:
            temp.pop(0)
        mem[last_num] = temp
    if k == 2020:
        break
    k += 1

print(last_num)
#part 2
file = open('input.txt', 'r')
l = file.read().strip().split(",")
l = list(map(int, l))
print(l)

mem = {}

for i,num in enumerate(l):
    mem[num] = [i+1]
    last_num = num
#last_num =16
k = len(l)+1
print(k)
while True:
    if k % 1000000 == 0:
        print(k)
    if last_num in mem.keys():
        if len(mem[last_num]) == 2:
            last_num = mem[last_num][1] - mem[last_num][0]
            if last_num in mem.keys():
                temp = mem[last_num]
                temp.append(k)
                if len(temp) == 3:
                    temp.pop(0)
                mem[last_num] = temp
            else:
                mem[last_num] = [k]
        else:
            last_num = 0
            temp = mem[last_num]
            temp.append(k)
            if len(temp) ==3:
                temp.pop(0)
            mem[last_num] = temp
    else:
        last_num = 0
        temp = mem[last_num]
        temp.append(k)
        if len(temp) ==3:
            temp.pop(0)
        mem[last_num] = temp
    if k == 30000000:
        break
    k += 1

print(last_num)
