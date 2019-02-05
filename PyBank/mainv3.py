import os
import csv

total_months = []
total_revenue =[]
avg_rev =[]
revenue = 0
index = 0

print("Financial Analysis")
print("------------------")


with open('budget_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(csvfile, None)

    
    for row in reader:
        total_months.append(row[0])
        total = len(list(total_months))

        
        revenue += int(row[1])
        total_revenue.append(row[1])
    print("Total Months: " + str(total))
    print("Total Revenue: $" + str(revenue))

    for i in range(len(total_revenue)):
        if i < (len(total_revenue)-1):
            avg_rev.append(int(total_revenue[i+1])-int(total_revenue[i]))
        y = sum(avg_rev)/int(len(avg_rev))
    print("Average Change in Revenue: ${:.0f}".format(y))

  
    greatest_increase = max(avg_rev)
    for z in avg_rev:
        if z == greatest_increase:
            max_date = int(avg_rev.index(z)) + 1

            print("Greatest Increase in Revenue: " + str(total_months[max_date]) +
                  " ($" + str(greatest_increase) + ")")


    
    greatest_decrease = min(avg_rev)
    for a in avg_rev:
        if a == greatest_decrease:
            min_date = int(avg_rev.index(a)) + 1

            print("Greatest Decrease in Revenue: " + str(total_months[min_date]) +
                  " ($" + str(greatest_decrease) + ")")

    
    #prof = (int(row[1]))
    #revall.append(row[1])
    
    #print("Total Revenue: " + str(revall))
    
    #revall += int(row[1])

    #print("Total Revenue: $" + str(revall))
    #print("Average Change: " +str(avgchg)) 



#print(len(bankplbudget))
#print(sum(avgchg)/len(avgchg))
#print(max avgchg)
    #print(avgchg)
