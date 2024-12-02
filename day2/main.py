file = open("input.txt", "rt")

safe_counter = 0
for line in file:
    numbers = [int(x) for x in line.split()]
    diffs = [i2 - i1 for i1, i2 in zip(numbers, numbers[1:])]
    is_increasing: bool
    if diffs[0] > 0:
        is_increasing = True
    else:
        is_increasing = False
        
    is_safe = True
    for d in diffs:
        if is_increasing and (d < 1 or d > 3):
            is_safe = False
            break
        elif not is_increasing and (d < -3 or d > -1):
            is_safe = False
            break

    if is_safe:
        safe_counter += 1
    
print(safe_counter)
# Part 2
safe_counter = 0
file.seek(0)

for line in file:
    numbers = [int(x) for x in line.split()]
    diffs = [i2 - i1 for i1, i2 in zip(numbers, numbers[1:])]
    is_increasing: bool
    if diffs[0] > 0:
        is_increasing = True
    else:
        is_increasing = False


    def diff_check():
        for i in range(len(diffs)):
            d = diffs[i]
            if is_increasing and (d < 1 or d > 3):
                return (False, i)
                break
            elif not is_increasing and (d < -3 or d > -1):
                return (False, i)
                break
        return (True, 0)

    is_safe, index = diff_check()
    if not is_safe:
        diffs.pop(index)
        is_safe, _ = diff_check()

    if is_safe:
        safe_counter += 1

print(safe_counter)
file.close()
