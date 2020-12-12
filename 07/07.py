file = open('input.txt', 'r')
l = file.read().splitlines()

bag_dict = {}

#method for reading line
def read_line(line):
    line = line.strip(".")
    bag = line.split("contain")[0][:-6]
    bag = bag.split()
    bag = bag[0] + " " + bag[1]
    contain = line.split("contain")[1].split(",")
    if contain == [" no other bags"]:
        contain = "no other"
    else:
        for i in range(0,len(contain)):
            temp = contain[i][1:-4]
            temp = temp.split()
            contain[i] = temp[1] + " " + temp[2]
    return (bag, contain)

def search(key,tot):
    if key in bag_dict.keys():
        if "shiny gold" in bag_dict[key]:
            return True
        for b in bag_dict[key]:
            found = search(b,tot)
            if found:
                return True
    else:
        return False

k = 0
total = 0
for line in l:
    print(k)
    bag, contain = read_line(line)
    #add to  bag_dict
    bag_dict[bag] = contain
    k+=1
    print(bag,contain)

for key in bag_dict.keys():
    found = search(key,0)
    if found:
        total += 1
print(total)

#part 2
file = open('input.txt', 'r')
l = file.read().splitlines()

bag_dict = {}

#method for reading line
def read_line_num(line):
    line = line.strip(".")
    bag = line.split("contain")[0][:-6]
    bag = bag.split()
    bag = bag[0] + " " + bag[1]
    contain = line.split("contain")[1].split(",")
    if contain == [" no other bags"]:
        contain = [{"name":"no other bags","num":0}]
    else:
        for i in range(0,len(contain)):
            temp = contain[i][1:-4]
            temp = temp.split()
            num = temp[0]
            bag_name = temp[1] + " " + temp[2]
            contain[i] = {"name":bag_name,"num":int(num)}
    return (bag, contain)

def count(key):
    global total
    if key in bag_dict.keys():
        for b in bag_dict[key]:
            for n in range(0,b["num"]):
                total += 1
                count(b["name"])
    return

k = 0
total = 0
for line in l:
    print(k)
    bag, contain = read_line_num(line)
    #add to  bag_dict
    bag_dict[bag] = contain
    k+=1
    print(bag,contain)


count("shiny gold")

print(total)
