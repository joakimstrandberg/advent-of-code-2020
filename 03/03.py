file = open('input.txt', 'r')
l = file.readlines()

l = [ line.strip() for line in l]
print(l)
delta_down=1
delta_right=3
right=0
down=0
num_trees = 0
travel= True

while(travel):
    #take step right
    right = (delta_right + right) % len(l[0])

    #takestep down
    down += delta_down

    print(down,right)
    #is_at_bottom?
    travel = (down < len(l))
    if travel:
        # is pos tree?
        if l[down][right] != ".":
            num_trees += 1

print(num_trees)


######### part 2 #########
#right,down
deltas = [[1,1],[3,1],[5,1],[7,1],[1,2]]
mult = 1
for d in deltas:
    print(l)
    delta_down=d[1]
    delta_right=d[0]
    right=0
    down=0
    num_trees = 0
    travel= True

    while(travel):
        #take step right
        right = (delta_right + right) % len(l[0])

        #takestep down
        down += delta_down

        print(down,right)
        #is_at_bottom?
        travel = (down < len(l))
        if travel:
            # is pos tree?
            if l[down][right] != ".":
                num_trees += 1
    mult *= num_trees
print(mult)
