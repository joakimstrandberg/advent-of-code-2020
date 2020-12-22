file = open('input.txt', 'r')
l = file.read().splitlines()

mem = {}

for line in l:
    line = line.split("=")
    if line[0][:4] == "mask":
        temp = line[1][1:]
        mask = temp
    if line[0][:3] == "mem":
        temp = line[0].split("[")
        temp = temp[1].split("]")
        address = int(temp[0])
        dec = line[1][1:]
        bin = "{0:b}".format(int(dec))
        s = ""
        for i in range(0,len(mask)-len(bin)):
            s = s + "0"
        bin = s + bin
        bin_list = list(bin)
        for i in range(0,len(mask)):
            if mask[i] != "X":
                bin_list[i] = mask[i]
        new_bin = "".join(bin_list)
        mem[address] = new_bin

tot_sum = 0
for k in mem.keys():
    tot_sum += int(mem[k],2)
print(tot_sum)

#Part 2
file = open('input.txt', 'r')
l = file.read().splitlines()

mem = {}
def gen_address(address,mask,gen):
    address_list = []
    if len(address) == 0:
        return [gen]
    if mask[0] == "X":
        address_list.extend(gen_address(address[1:],mask[1:],gen+"1"))
        address_list.extend(gen_address(address[1:],mask[1:],gen+"0"))
    elif mask[0] == "1":
        address_list.extend(gen_address(address[1:],mask[1:],gen+mask[0]))
    else:
        address_list.extend(gen_address(address[1:],mask[1:],gen+address[0]))
    return address_list


for line in l:
    line = line.split("=")
    if line[0][:4] == "mask":
        temp = line[1][1:]
        #mask = [i == "1" for i in temp]
        mask = temp
    if line[0][:3] == "mem":
        temp = line[0].split("[")
        temp = temp[1].split("]")
        address = int(temp[0])
        address_bin = "{0:b}".format(int(address))
        dec = int(line[1][1:])
        #pad address with 0
        s = ""
        for i in range(0,len(mask)-len(address_bin)):
            s = s + "0"
        address_bin = s+address_bin
        print("address ", address_bin)
        print("mask    ", mask)
        address_list = gen_address(address_bin,mask,"")
        print(len(address_list))
        for a in address_list:
            mem[a] = dec

tot_sum = 0
for k in mem.keys():
    tot_sum += mem[k]
print(tot_sum)
