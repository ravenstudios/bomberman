f = open("map.map")
# print(f.read())
m = f.read()
# print(m)
f.close()

map_list = m.split("\n")


for m in range(len(map_list)):
    temp = map_list[m].split(",")
    map_list[m] = temp

for r in range(len(map_list)):
    print(map_list[r])

result = []

for r in range(len(map_list)):
    temp = []
    for c in range(len(map_list[r])):

        if map_list[r][c] == "0":
            temp.append("S")
        elif map_list[r][c] == "1":
            temp.append("D")
        elif map_list[r][c] == "2":
            temp.append("G")
        elif map_list[r][c] == "3":
            temp.append("W")
    result.append(temp)


for r in range(len(result)):
    print(result[r])
