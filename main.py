import secrets
import json
from flask import Flask,render_template,request
from flask import json as flajson
from flaskext.mysql import MySQL

secret_key = secrets.token_hex()

mysql = MySQL()
app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "abcdefgh"
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def index():
   if request.method=='POST':
      name=request.form['uname']
      username=request.form['userName']
      passw=request.form['userPassword']
      sqlcon=mysql.connect()
      db=sqlcon.cursor()
      db.execute("SELECT * FROM USERS where username='"+username+"'")  # For Selection
      k=db.rowcount
      db.close()
      if k==0:
        db=sqlcon.cursor()
        db.execute('INSERT INTO USERS VALUES(%s,%s,%s)',(name,username,passw))
        sqlcon.commit()
        db.close()
      else:
         return "Username already taken, please select a different one."
      return render_template('index.html')

   return render_template('index.html')

@app.route('/signup.html',methods=['GET','POST'])
def newuser():
   return render_template('signup.html')

@app.route('/login.html',methods=['GET','POST'])
def login():

   return render_template('login.html')


@app.route('/fileload.html',methods=['GET','POST'])
def fileload():

   if request.method=='POST':
      username=request.form['userName']
      passw=request.form['userPassword']
      sqlcon=mysql.connect()
      db=sqlcon.cursor()
      db.execute("SELECT * FROM USERS where username='"+username+"' and passw='"+passw+"'")  # For Selection
      k=db.rowcount
      db.close()
      if k==0:
         return "Either the username or the password entered is wrong. Kindly double check."
      elif k==1:
         return render_template('fileload.html',username=username)
      else:
         return "More than 1 user with the same credentials are present."


   return render_template('fileload.html')

@app.route('/result.html', methods = ['GET', 'POST'])
def res():
   if request.method == 'POST':
      f = request.files['jsonfile']
      fin=open(f.filename,'r')
      array=json.loads(fin.read())

      sqlcon=mysql.connect()
      db=sqlcon.cursor()
      for i in array: 
         userId=str(i["userId"])
         uid=str(i["id"])
         title=i["title"]
         body=i["body"]
         db.execute('INSERT INTO JSON_FILE VALUES(%s,%s,%s,%s)',(userId,uid,title,body))
         sqlcon.commit()
      db.close()
      prompt='File uploaded successfully.'
      return render_template('result.html',msg=prompt)


@app.route('/jsondata.html', methods = ['GET', 'POST'])
def getData():
   if request.method == 'POST':
      sqlcon=mysql.connect()
      db=sqlcon.cursor()
      users=db.execute("SELECT * FROM JSON_FILE") 
      if users>0:
         userData=db.fetchall()
         db.close()
         return render_template('jsondata.html',userData=userData)
    	
if __name__ == '__main__':
   app.run(debug=True)

