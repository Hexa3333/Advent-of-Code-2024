leftList = []
rightList = []

file = open("input.txt", "rt")
for line in file:
    split = line.split()
    leftList.append(int(split[0]))
    rightList.append(int(split[1]))

file.close()

leftList.sort()
rightList.sort()

distance = 0
for i in range(len(leftList)):
    distance += abs(leftList[i] - rightList[i])

print("1: " + str(distance))

# Part 2
similarities = dict()

for n in leftList:
    nScore = similarities.setdefault(n, 0)
    nScore += n * rightList.count(n)
    similarities[n] = nScore

similarity_sum = 0
for x in similarities.values():
    similarity_sum += x

print("2: " + str(similarity_sum))
