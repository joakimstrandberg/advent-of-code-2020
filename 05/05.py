file = open('input.txt', 'r')
l = file.read().splitlines()

highest_score = 0

for line in l:
    row_string = line.replace("B","1")
    row_string = row_string.replace("F","0")
    row_string = row_string.replace("R","1")
    row_string = row_string.replace("L","0")

    #to dec
    row = int(row_string[:-3],2)
    col = int(row_string[-3:],2)

    score = row*8+ col
    if score > highest_score:
        highest_score = score

print(highest_score)

#part 2
id_list = []
for line in l:
    row_string = line.replace("B","1")
    row_string = row_string.replace("F","0")
    row_string = row_string.replace("R","1")
    row_string = row_string.replace("L","0")

    row_int = int(row_string,2)
    id_list.append(row_int)
id_list.sort()
for i in range(0,len(id_list[:-1])-1):
    if not id_list[i+1] - id_list[i] == 1:
        print(id_list[i],id_list[i+1])
        break
