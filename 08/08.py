file = open('input.txt', 'r')
l = file.read().splitlines()

acc = 0
print(l[0:10])
index = 0
index_set = set()
while True:
    if index in index_set:
        break
    index_set.add(index)
    #fetch instruction
    instruction = l[index]
    #decode instruction
    instruction = instruction.split()
    code = instruction[0]
    value = int(instruction[1])
    #execute
    if code == "acc":
        acc += value
    elif code == "jmp":
        index += value
        continue
    index +=1
print(acc)

#part 2
nop_i = [i for i,item in enumerate(l) if item[:3] == "nop"]
change_list = [i for i,item in enumerate(l) if item[:3] == "jmp"]
change_list.extend(nop_i)

for i in change_list:
    acc = 0
    index = 0
    index_set = set()
    while True:
        if index == len(l):
            print("CORRECT")
            print(acc)
            break
        if index in index_set:
            break
        index_set.add(index)
        #fetch instruction
        instruction = l[index]
        #decode instruction
        instruction = instruction.split()
        code = instruction[0]
        value = int(instruction[1])
        #execute
        if index == i:
            if code == "jmp":
                code = "nop"
            elif code == "nop":
                code = "jmp"
        if code == "acc":
            acc += value
        elif code == "jmp":
            index += value
            continue
        index +=1
