import os
import csv
bankplbudget = {}
totalmo=0
prof =0
lastpl=0
totalmo = []
plchg = []
avgchg = 0
revall = []


with open('budget_data.csv') as csvfile:
   
    reader = csv.reader(csvfile, delimiter=",")
    next(csvfile,None)
    print("Financial Analysis")
    print("__________________")

    for row in reader:
        totalmo.append(row[0])
    
    
        bankplbudget[row[0]]=int(row[1])
        if lastpl!=0: 
            if int(row[1])<0 or lastpl<0:
                plchg.append(int(row[1]) + lastpl)
            elif int(row[1])>lastpl:
                plchg.append(int(row[1]) - lastpl)
            else:
                plchg.append(lastpl - int(row[1]))
        lastpl=(int(row[1]))
        totalallmo =len(totalmo)
        
        #avgchg=(totalmo / len(plchg))

    print("Total Months: " + str(totalallmo))

    #avgchg = sum((plchg)//int(totalallmo)
    
    prof += (int(row[1]))
    revall.append(row[1])
    print("Total Revenue: " + str([revall))
    
    #revall += int(row[1])

    #print("Total Revenue: $" + str(revall))
    #print("Average Change: " +str(avgchg)) 



#print(len(bankplbudget))
#print(sum(avgchg)/len(avgchg))
#print(max avgchg)
    #print(avgchg)
