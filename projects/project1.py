numDays = float(input("enter number of days temparature?  : "))
total = 0
for i in range(1,numDays+1):
    nextDay = float(input("Day"+str(i)+"'s temparure : "))
    total+=nextDay

avg = round(total/numDays,2)
print("\n Average = "+str(avg))