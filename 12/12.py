file = open('input.txt', 'r')
l = file.read().splitlines()
import math

pos_dict = {"N":0,"E":0}
action_dict = {"N":1,"S":-1,"E":1,"W":-1}
dir = 0
dir_dict = {0:"E",1:"S",2:"W",3:"N"}

for line in l:
    action = line[0]
    value = int(line[1:])

    if action == "N" or action == "S":
        pos_dict["N"] += action_dict[action]*value
    elif action == "E" or action == "W":
        pos_dict["E"] += action_dict[action]*value
    elif action =="R":
        dir = (dir + (value / 90) ) % 4
    elif action =="L":
        dir = (dir - (value / 90) ) % 4
    elif action == "F":
        if dir_dict[dir] == "E" or dir_dict[dir] == "W":
            pos_dict["E"] += action_dict[dir_dict[dir]]*value
        else:
            pos_dict["N"] += action_dict[dir_dict[dir]]*value

manhattan = abs(pos_dict["N"]) + abs(pos_dict["E"])
print(manhattan)
#Part 2
file = open('input.txt', 'r')
l = file.read().splitlines()

pos_dict = {"N":0,"E":0}
w_dict = {"N":1,"E":10}
action_dict = {"N":1,"S":-1,"E":1,"W":-1}

def rot(x,y,deg,clock):
    n = deg // 90
    sign_sin = {0:1,1:1,2:-1,3:-1}
    sign_cos = {0:1,1:-1,2:-1,3:1}
    if not clock:
        newx = (sign_cos[n]*(x * ((n+1) % 2)) - sign_sin[n]*(y * ((n) % 2)))
        newy = (sign_sin[n]*(x * ((n) % 2)) + sign_cos[n]*(y * ((n+1) % 2)))
    else:
        newx = (sign_cos[n]*(x * ((n+1) % 2)) + sign_sin[n]*(y * ((n) % 2)))
        newy = (- sign_sin[n]*(x * ((n) % 2)) + sign_cos[n]*(y * ((n+1) % 2)))
    return (newx,newy)

for line in l:
    action = line[0]
    value = int(line[1:])

    if action == "N" or action == "S":
        w_dict["N"] += action_dict[action]*value
    elif action == "E" or action == "W":
        w_dict["E"] += action_dict[action]*value
    elif action =="R":
        x,y = rot(w_dict["E"],w_dict["N"],value,True)
        w_dict["E"] = x
        w_dict["N"] = y
    elif action =="L":
        print("before ", w_dict["E"]," ",w_dict["N"])
        print("rot ",action, " ", value)
        x,y = rot(w_dict["E"],w_dict["N"],value,False)
        w_dict["E"] = x
        w_dict["N"] = y
        print("after ", w_dict["E"]," ",w_dict["N"])
        print("")
    elif action == "F":
        pos_dict["E"] += w_dict["E"]*value
        pos_dict["N"] += w_dict["N"]*value

manhattan = abs(pos_dict["N"]) + abs(pos_dict["E"])
print(manhattan)
