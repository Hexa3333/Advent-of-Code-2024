# Re✝arded solution
file = open("input.txt", "rt")
# Part 1
result = 0
for line in file:
    while line.find("mul(") != -1:
        mul_found = line.find("mul(")
        buf = line[mul_found+4:mul_found+12]
        X = ""
        Y = ""
        corrupted = False
        opno = 1
        for c in buf:
            if c.isnumeric():
                if opno == 1:
                    X += c
                elif opno == 2:
                    Y += c
            elif c == ',':
                opno += 1
                if opno > 2:
                    corrupted = True
                    break
            elif c == ')':
                if not X or not Y:
                    corrupted = True
                break
            else:
                corrupted = True
                break

        if not corrupted:
            result += int(X) * int(Y)

        # move line forwards
        line = line[mul_found+4:]
        

print(result)

# Part 2
result = 0
file.seek(0)
do_enabled = True

for line in file:
    while line.find("mul(") != -1:
        mul_found = line.find("mul(")

        # >>> 1 -> -1 becomes and impossibly big value
        do_found = line.find("do()")
        dont_found = line.find("don\'t()")

        if do_enabled and dont_found != -1 and dont_found < mul_found:
            do_enabled = False
        elif not do_enabled and do_found != -1 and do_found < mul_found:
            do_enabled = True

        buf = line[mul_found+4:mul_found+12]
        X = ""
        Y = ""
        corrupted = False
        opno = 1
        for c in buf:
            if c.isnumeric():
                if opno == 1:
                    X += c
                elif opno == 2:
                    Y += c
            elif c == ',':
                opno += 1
                if opno > 2:
                    corrupted = True
                    break
            elif c == ')':
                if not X or not Y:
                    corrupted = True
                break
            else:
                corrupted = True
                break

        if do_enabled and not corrupted:
            result += int(X) * int(Y)

        # move line forwards
        line = line[mul_found+4:]

print(result)
file.close()
