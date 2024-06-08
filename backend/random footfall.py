import csv
import random
f1 = open('footfall data.csv', 'r')
allrec = csv.reader(f1)
header_row = next(allrec)
list1=[]
for b in allrec:
     list1+=[b]
for rec in list1:
     for k in range (3,14):
          n=int(rec[k])
          rec[k]=random.randrange(n-5,n+5)        
f1.seek(0)
f2= open('footfall data2.csv','w',newline='')
a=csv.writer(f2,delimiter=',')
for j in list1:
     a.writerow(j)
     f2.flush()  
f1.close()     
