numDays = int(input("enter number of days temparature?  : "))
total = 0
temp = []
for i in range(numDays):
    nextDay = float(input("Day"+str(i+1)+"'s temparure : "))
    temp.append(nextDay)
    total += temp[i]
    print(total)

avg = round(total/numDays,2)
print("\n Average = "+str(avg))

above = 0

for i in temp:
    if i > avg:
        above+=1
print(f"The number of days above {avg} are :",above)