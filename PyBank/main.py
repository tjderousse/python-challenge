import os
import csv
bankplbudget = {}
total_pl=0
lastpl=0
plchg = []
avgchg = []

with open('budget_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(csvfile,None)
    for row in reader:
        total_pl=total_pl + int(row[1])
        bankplbudget[row[0]]=int(row[1])
        if lastpl!=0: 
            if int(row[1])<0 or lastpl<0:
                plchg.append(int(row[1]) + lastpl)
            elif int(row[1])>lastpl:
                plchg.append(int(row[1]) - lastpl)
            else:
                plchg.append(lastpl - int(row[1]))
        lastpl=(int(row[1]))
        avgchg=(sum(plchg)/len(plchg))



#print(len(bankplbudget))
#print(sum(avgchg)/len(avgchg))
#print(max avgchg)
print(avgchg)



      
