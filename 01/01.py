file = open('input.txt', 'r')
l = file.readlines()
l = [ int(line.strip()) for line in l]
print l

num = 0
for i in l:
    for j in l:
        if i + j == 2020:
            print j * i
            break

### part 2
for i in l:
    for j in l:
        for k in l:
            if i + j +k == 2020:
                print j * i * k
