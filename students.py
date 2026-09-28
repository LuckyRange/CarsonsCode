file = open("students.txt")
while True: 
  lastName = (file.readline)

if: break

district = (file.readline)
credits = (file.readline)

if district == "I":
  costPerCredit = 250
else:
  costPerCredit = 500

tuition = credits * costPerCredit
studentCount = 1

print("Total Tuition", tuition)
print("Number Of Students", studentCount)
