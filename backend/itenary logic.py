import mysql.connector
import random
import datetime

state = 'gujarat'
city= 'ahmedabad'
arrival="07-24-2024" #month,day,year
departure="07-25-2024"
l=arrival.split('-')
date=datetime.datetime(int(l[2]),int(l[0]),int(l[1]))#year,month,day
e=departure.split('-')
date2=datetime.datetime(int(e[2]),int(e[0]),int(e[1]))#year,month,day
dates=[]
if date2.isoweekday()> date.isoweekday():
     r=(date2.isoweekday()-date.isoweekday())
elif date2.isoweekday()<date.isoweekday():
     r=7-date.isoweekday()+date2.isoweekday()
elif date2.isoweekday()==date.isoweekday():
     r=7
for q in range(r+1):
          d=date.isoweekday()+q
          if d>7:
               d=d-7
          dates+=[d],
days=len(dates)
for i in range(days):
     if dates[i]==[1]:
          dates[i]='Monday'
     elif dates[i]==[2]:
          dates[i]='Tuesday'
     elif dates[i]==[3]:
          dates[i]='Wednesday'
     elif dates[i]==[4]:
          dates[i]='Thursday'
     elif dates[i]==[5]:
          dates[i]='Friday'
     elif dates[i]==[6]:
          dates[i]='Saturday'
     elif dates[i]==[7]:
          dates[i]='Sunday'
mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
mycursor=mydb.cursor()
mycursor.execute("USE SMARTDESTINA")
mycursor.execute("SELECT * from data where city='"+city+"'")
myrecords=mycursor.fetchall()
places=[]
for x in myrecords:
     places+=[x]
mrng=[]
eve=[]
noon=[]
al=[]
for i in places:
     if (i[7].lower()).strip()=='morning':
          mrng+=[i]
     elif (i[7].lower()).strip()=='afternoon':
          noon+=[i]
     elif (i[7].lower()).strip()=='evening':    
          eve+=[i]      
     elif (i[7].lower()).strip()=='all':
          al+=[i]          
random.shuffle(mrng)
random.shuffle(eve)
random.shuffle(noon)
random.shuffle(al)
it=[]
for b in range(days):
     it+=[],
while len(mrng)!=0 and len(eve)!=0 and len(noon)!=0:
     c=[]
     for b in it:
          c+=[len(b)]
     count=c.index(min(c))
     if len(mrng)!=0 and dates[count]!=mrng[-1][5]:
          
          it[count]+=[mrng.pop()]
     count=c.index(min(c))
     if len(noon)!=0 and dates[count]!=noon[-1][5]:
          it[count]+=[noon.pop()]
     count=c.index(min(c))
     if len(eve)!=0 and dates[count]!=eve[-1][5]:
          it[count]+=[eve.pop()]
while len(al)!=0:
     c=[]
     for b in it:
          c+=[len(b)]
     count=c.index(min(c))
     if dates[count]!=al[-1][5]:
          it[count]+=[al.pop()]
output=[]  
count=0
for k in it:
     out=[]
     count+=1 
     for p in k: 
          out2=[]
          out2+=p[3],p[7],float(p[9]),float(p[10]),float(p[11])
          sqmt="SELECT * from fdata where name='"+p[3]+"'"
          mycursor.execute(sqmt)
          myrecords=mycursor.fetchall()
          for y in myrecords:
               if p[7].lower()=='morning':
                    out2+=y[2],y[5],y[8],y[11],float(y[14])
               if p[7].lower()=='afternoon':
                    out2+=y[3],y[6],y[9],y[12],float(y[14])
               if p[7].lower()=='evening':
                    out2+=y[4],y[7],y[10],y[13],float(y[14])
               if p[7].lower()=='all':
                    out2+=y[2:]
          out+=[out2],    
     output+=out,
count=1
for f in output:
     print("DAY",count,":")
     for s in f:
          print()
          print("Place:",[s][0][0][0])
          if ([s][0][0][1].lower()).strip()=='all':
               print("Best time to visit:",[s][0][0][1])
               if date.month in range(5,10):
                    if(date.isoweekday()+count in range(1,5+1)):
                         if[s][0][0][8]<[s][0][0][14]:
                              print("Footfall in morning: LOW")
                         else:
                              print("Footfall in morning: HIGH")
                         if[s][0][0][9]<[s][0][0][14]:
                              print("Footfall in afternoon: LOW")
                         else:
                              print("Footfall in afternoon: HIGH")
                         if[s][0][0][10]<[s][0][0][14]:
                              print("Footfall in evening: LOW")
                         else:
                              print("Footfall in evening: HIGH")
                    else:
                         if[s][0][0][11]<[s][0][0][14]:
                              print("Footfall in morning: LOW")
                         else:
                              print("Footfall in morning: HIGH")
                         if[s][0][0][12]<[s][0][0][14]:
                              print("Footfall in afternoon: LOW")
                         else:
                              print("Footfall in afternoon: HIGH")
                         if[s][0][0][13]<[s][0][0][14]:
                              print("Footfall in evening: LOW")
                         else:
                              print("Footfall in evening: HIGH")
               else:
                    if(date.isoweekday()+count in range(1,5+1)):
                         if[s][0][0][2]<[s][0][0][14]:
                              print("Footfall in morning: LOW")
                         else:
                              print("Footfall in morning: HIGH")
                         if[s][0][0][3]<[s][0][0][14]:
                              print("Footfall in afternoon: LOW")
                         else:
                              print("Footfall in afternoon: HIGH")
                         if[s][0][0][4]<[s][0][0][14]:
                              print("Footfall in evening: LOW")
                         else:
                              print("Footfall in evening: HIGH")
                    else:
                         if[s][0][0][5]<[s][0][0][14]:
                              print("Footfall in morning: LOW")
                         else:
                              print("Footfall in morning: HIGH")
                         if[s][0][0][5+1]<[s][0][0][14]:
                              print("Footfall in afternoon: LOW")
                         else:
                              print("Footfall in afternoon: HIGH")
                         if[s][0][0][7]<[s][0][0][14]:
                              print("Footfall in evening: LOW")
                         else:
                              print("Footfall in evening: HIGH")
          else:
               print("Best time to visit:",[s][0][0][1])
          print("Time to spend:",[s][0][0][2],"hours")
          print("Rating:",[s][0][0][3])
          print("Entry Fee:",[s][0][0][4])
     print()
     count+=1
