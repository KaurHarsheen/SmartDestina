import mysql.connector
import random
import datetime


from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
     state = request.form['state']
     city = request.form['city']
     
     arrival="07-22-2024"#month,day,year
     departure="07-25-2024"
     l=arrival.split('-')
     date=datetime.datetime(int(l[2]),int(l[0]),int(l[1]))#year,month,day
     e=departure.split('-')
     date2=datetime.datetime(int(e[2]),int(e[0]),int(e[1]))#year,month,day
     dates=[]
     print(date.isoweekday(),date2.isoweekday())

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
     mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="SMARTDESTINA")
     mycursor=mydb.cursor()
     #mycursor.execute("USE SMARTDESTINA")
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
          if i[7].lower()=='morning':
               mrng+=[i]
          elif i[7].lower()=='afternoon':
               noon+=[i]
          elif i[7].lower()=='evening':
               eve+=[i]
          elif i[7].lower()=='all':
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

     o1=[],o2=[]         
     for k in it:
          for f in k:
               o1+=f[3]
          o2+=[len(k)]
     o1=','.join(o1)
     o2=','.join(o2)
     return redirect('/result?state={}&city={}'.format(o1, o2))
    
@app.route('/result')
def result():
    state = request.args.get('state')
    city = request.args.get('city')
    
    return render_template('result.html', state=state, city=city)
if __name__ == '__main__':
    app.run(debug=True)

