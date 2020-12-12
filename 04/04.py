file = open('input.txt', 'r')
l = file.read().splitlines()
sum_valid = 0
ctrl = {"byr":False,"iyr":False, "eyr":False, "hgt":False, "hcl":False , "ecl":False, "pid":False}
for line in l:
    if line != "":
        strip = line.split()
        #print(strip)
        for s in strip:
            #split on :
            key = s.split(":")[0]
            if key in ctrl.keys():
                ctrl[key] = True
    else:
        if False not in ctrl.values():
            sum_valid += 1
        #reset ctrl
        for key in ctrl.keys():
            ctrl[key] = False


print(sum_valid)

#Part 2
debug = {}
sum_valid = 0
ctrl = {"byr":False,"iyr":False, "eyr":False, "hgt":False, "hcl":False , "ecl":False, "pid":False}
for index, line in enumerate(l):
    if line != "":
        strip = line.split()
        #print(strip)
        for s in strip:
            #split on :
            key = s.split(":")[0]
            value = s.split(":")[1]
            debug[key] = value
            #rules
            if key == "byr":
                if int(value) <= 2002 and int(value) >= 1920:
                    ctrl[key] = True
            if key == "iyr":
                if int(value) <= 2020 and int(value) >= 2010:
                    ctrl[key] = True
            if key == "eyr":
                if int(value) <= 2030 and int(value) >= 2020:
                    ctrl[key] = True
            if key == "hgt":
                if value[-2:] == "in":
                    if int(value[:-2]) <= 76 and int(value[:-2]) >= 59:
                        ctrl[key] = True
                elif value[-2:] == "cm":
                    if int(value[:-2]) <= 193 and int(value[:-2]) >= 150:
                        ctrl[key] = True
            if key == "hcl":
                okay = True
                if value[0]=="#" and len(value[1:]) == 6:
                    for v in value[1:]:
                        if v not in ["a","b","c","d","e","f","1","2","3","4","5","6","7","8","9","0"]:
                            okay = False
                            break
                    if okay:
                        ctrl[key] = True
            if key == "ecl":
                if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    ctrl[key] = True
            if key == "pid":
                if value.isnumeric() and len(value)==9 :
                    ctrl[key] = True

    else:
        if False not in ctrl.values():
            sum_valid += 1
        else:
            ks = [k for k in ctrl.keys() if not ctrl[k]]
            print("### false ### line: {}".format(index))
            for k in ks:
                if k in debug.keys():
                    print(k,debug[k], end=' ', flush=True)
            print("")
        #reset ctrl
        for key in ctrl.keys():
            ctrl[key] = False
            debug = {}

print(sum_valid)
