players = ()

file = open("module12And13Problem6.txt", "r")

for line in file
name, average = line.split()
players(name) = float(average)

file.close()

print("Name; Batting Average")

for name in players
print(name, players(name))
