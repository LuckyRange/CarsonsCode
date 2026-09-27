file = open("employee.txt")
while True:
  lastName = (file.readline)

salary = (file.readline)
if salary >= 100000:
  bonusRate = 0.20
elif salary >= 50000:
  bonusRate = 0.15 
else:
  bonusRate = 0.10

bonus = salary * bonusRate
totalBonus + = bonus

Print(lastName, salary, bonus)
