file = open('input.txt', 'r')
l = file.read().splitlines()
print(len(l[1].split(",")))

timestamp = int(l[0])
bus_id_list = [int(i) for i in l[1].split(",") if i != "x"]
print(bus_id_list)
print(timestamp)

bus_arrived = False

bus_id = 0
k = 0
min_waited = 0
while not bus_arrived:
    for id in bus_id_list:
        if (timestamp + k) % id == 0:
            bus_id = id
            bus_arrived = True
            min_waited = k
            break
    k += 1
print(min_waited*bus_id)
#Part 2
#all ids are primes
file = open('input.txt', 'r')
l = file.read().splitlines()

bus_id_offset_dict = dict([[int(id),-i] for i,id in enumerate(l[1].split(",")) if id != "x"])
print(bus_id_offset_dict)

#Chinese remainder
found = False
mult_dict = {}
for id in bus_id_offset_dict.keys():
    n = 1
    mult = 1
    for i in bus_id_offset_dict.keys():
        if id == i:
            continue
        mult = mult* i
    while not found:
        if n* mult % id == 1:
            mult_dict[id] = n*mult
            break
        n += 1
# add all
add = 0
mult = 1
for id in bus_id_offset_dict.keys():
    add += mult_dict[id]*bus_id_offset_dict[id]
    mult = mult* id

print(add % mult)

def render(timestamp,end,bus_dict):
    print("    ", sep=' ', end='', flush=True)
    for id in bus_dict.keys():
        print(" {}".format(id), sep=' ', end='', flush=True)
    for i in range(0,end):
        print("")
        print(timestamp+i, sep=' ', end='', flush=True)
        for id in bus_dict.keys():
            if (timestamp+i) % id == 0:
                print("  D", sep=' ', end='', flush=True)
            else:
                print("  .", sep=' ', end='', flush=True)
render(add % mult,200,bus_id_offset_dict)
