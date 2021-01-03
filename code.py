from flask import Flask, render_template,request,json, session, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dateutil import parser
from flask_mail import Mail
from sqlalchemy import text
#pip install -U Werkzeug
#pip3 install flash
#pip3 install flask-sqlalchemy
from werkzeug.utils import secure_filename
import os,csv,requests,math,atexit,pathlib
from apscheduler.schedulers.background import BackgroundScheduler

#pip install pymysql
app = Flask(__name__)
app.secret_key ='super-secret-key'

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "config.json"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path,'r') as f1:
		p=json.load(f1)["params"]

app.config['UPLOAD_FOLDER'] = p['upload_location']
app.config.update(
		MAIL_SERVER = 'smtp.gmail.com',
		MAIL_PORT = '465',
		MAIL_USE_SSL = True,
		MAIL_USERNAME = p['gmail-user'],
		MAIL_PASSWORD=  p['gmail-password'])
mail = Mail(app)

local_server = True
if(local_server):
		app.config['SQLALCHEMY_DATABASE_URI'] = p['local_uri']
else:
		app.config['SQLALCHEMY_DATABASE_URI'] = p['prod_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Database table properties
class Contacts(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(80), nullable=False)
		phone_num = db.Column(db.String(12), nullable=False)
		msg = db.Column(db.String(120), nullable=False)
		date = db.Column(db.String(12), nullable=True)
		email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		title = db.Column(db.String(80), nullable=False)
		slug = db.Column(db.String(21), nullable=False)
		author = db.Column(db.String(50), nullable=True)
		content = db.Column(db.String(420), nullable=False)
		date = db.Column(db.String(12), nullable=True)
		img_file = db.Column(db.String(12), nullable=True)
		tagline = db.Column(db.String(100), nullable=False)

@app.route("/",methods=['GET','POST'])
def home():
		#flash("THis is flash message. You can close them.", "success")
		#flash("Lots more to come yet.", "danger")
	author_name = 'Praveen Gupta'
	if request.method == 'POST':
		author_name=request.form.get('authorname')
		if author_name == 'NULL':
				posts = Posts.query.filter_by().order_by(text("date desc")).all()
		else:
			posts = Posts.query.filter_by(author=author_name).order_by(text("date desc")).all()

		last = math.ceil(len(posts)/int(p['no_of_posts']))
		#[0:p['no_of_posts']]
		page = request.args.get('page')
		if ( not str(page).isnumeric()):
				page = 1
		page = int(page)
		posts=posts[(page-1)*int(p['no_of_posts']):(page-1)*int(p['no_of_posts'])+int(p['no_of_posts'])]
		#pagination logic
		# First Page
		if (page==1):
				prev = "#"
				next ="/?page=" +str(page+1)
		elif (page==last):
				prev ="/?page=" +str(page-1)
				next ="#"
		else:
				prev ="/?page=" +str(page-1)
				next ="/?page=" +str(page+1)

		return render_template('index.html',params=p,posts=posts,prev=prev,next=next)
	else:
		posts = Posts.query.filter_by().order_by(text("date desc")).all()
		last = math.ceil(len(posts)/int(p['no_of_posts']))
		#[0:p['no_of_posts']]
		page = request.args.get('page')
		if ( not str(page).isnumeric()):
				page = 1
		page = int(page)
		posts=posts[(page-1)*int(p['no_of_posts']):(page-1)*int(p['no_of_posts'])+int(p['no_of_posts'])]
		#pagination logic
		# First Page
		if (page==1):
				prev = "#"
				next ="/?page=" +str(page+1)
		elif (page==last):
				prev ="/?page=" +str(page-1)
				next ="#"
		else:
				prev ="/?page=" +str(page-1)
				next ="/?page=" +str(page+1)

		return render_template('index.html',params=p,posts=posts,prev=prev,next=next)


@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
		post = Posts.query.filter_by(slug=post_slug).first()
		return render_template('post.html',params=p,post=post)


@app.route("/about")
def about():
		return render_template('about.html',params=p)

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():

		if ('user' in session and session['user'] == p['admin_user']):
				posts=Posts.query.all()
				return render_template('dashboard.html',params=p,posts=posts)

		if request.method == 'POST':
				username = request.form.get('uname')
				userpass = request.form.get('pass')
				if username == p['admin_user'] and userpass == p['admin_password']:
				# set session varaible
						session['user'] = username
						posts=Posts.query.all()
						return render_template('dashboard.html',params=p,posts=posts)
		else:
					return render_template('sign.html',params=p)

#edit post via html
@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
		if ('user' in session and session['user'] == p['admin_user']):
				if request.method == "POST":
						box_text=request.form.get('title')
						tagline=request.form.get('tagline')
						slug=request.form.get('slug')
						content=request.form.get('content')
						img_file=request.form.get('img_file')
						date = datetime.now()
						author = request.form.get('Author')
						if sno == '0':
								post = Posts(title=box_text, slug=slug,tagline=tagline,content=content,img_file=img_file,date=date,author=author)
								db.session.add(post)
								db.session.commit()
								flash("Your post is updated. Please using syntax post/slug", "success")
						else:
								post = Posts.query.filter_by(sno=sno).first()
								post.title=box_text
								post.slug=slug
								post.tagline=tline
								post.content=content
								post.img_file=img_file
								post.date=date
								db.session.commit()
								return redirect ('/edit/'+sno)
		post = Posts.query.filter_by(sno=sno).first()
		return render_template('edit.html',params=p, post=post,sno=sno)

class aqi(db.Model):
		sno = db.Column(db.Integer, primary_key=True)
		cityname = db.Column(db.String(50), nullable=False)
		citypincode = db.Column(db.Integer, nullable=True)

path=pathlib.Path(__file__).parent.absolute()
#path="/media/praveen/01D5D19062C0B570/Learning/Online Python/Module2/AutosavingCSV"
filename="aqi_temp_7days.csv"
filepath=os.path.join(path,filename)

scheduler = BackgroundScheduler()

def getDataAqi(city):
	url='https://api.waqi.info'
	pa={'token':p['api_key']}
	resp = requests.get(url + f"/feed/{city}/",params=pa)
	return resp.json()

def SaveInCsv():
	city='Pune'
	city_aqi_temp_date_time=[]
	data1=getDataAqi(city)
	city_aqi_temp_date_time.append(city)
	current_date = datetime.now().strftime("%d")
	city_aqi_temp_date_time.append(current_date)
	current_time = datetime.now().strftime("%H")
	city_aqi_temp_date_time.append(current_time)
	if data1['status']=="ok":
		aqi=data1['data']['aqi']
		cityactual=data1['data']['city']['name']
		temp=data1['data']['iaqi']['t']['v']
		city_aqi_temp_date_time.append(aqi)
		city_aqi_temp_date_time.append(temp)
		with open(filepath,'a') as f3:
			writer=csv.writer(f3)
			writer.writerow(city_aqi_temp_date_time)

#scheduler.add_job(func=SaveInCsv, trigger="interval", seconds=10)
#scheduler.start()
# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())
#pip install flask-requests
def cityaqi(city):
		#city='india/ghaziabad/vasundhara'
		#url='https://api.waqi.info'
		#pa={'token':'bd468662db1cfc6677641063ea0438656502e034'}
		#resp = requests.get(url + f"/feed/{city}/",params=pa)  # city is variable & token is param
		#data1=resp.json()
		data1=getDataAqi(city)
		if data1['status']=="ok":
				aqi=data1['data']['aqi']
				#t2=data1['data']['time']['s']
				t2=data1['data']['time']['s']
				#time2=parser.parse(time1)
				#t2=datetime.strftime('%H:%M:%S.%f',time2)
		else:
				aqi="NULL"
				t2 = "NULL"
		return aqi,t2

@app.route("/aqi", methods=['GET','POST'])
def aqi():
		if request.method == "POST":
				box_text=request.form.get('cityname')
				aqi,ti=cityaqi(box_text)
				return render_template('aqi.html',params=p,aqi=aqi,time=ti,city=box_text,method="NULL")
		else:
			with open(filename,'r') as f2:
				readr=csv.reader(f2)
				for i in readr:
					if i[0]==p['fix_city']:
						print("Temperature of the day",i[3])
						city_csv=i[0]
						aqi_csv = i[3]
						aqi_temp= i[4]
				return render_template('aqi.html',params=p, method="GET",city_csv=city_csv,aqi_csv=aqi_csv,aqi_temp=aqi_temp)
		#       box_text=request.form.get('cityname')
		#       adi=cityaqi(box_text)


# Uploader file
@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
		if ('user' in session and session['user'] == p['admin_user']):
				if (request.method == 'POST'):
						f=request.files['file1']
						f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename) ))
						return "Uploaded succesfully"

@app.route("/logout")
def logout():
		session.pop('user')
		return redirect ('/dashboard')

#Delete
@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
		if ('user' in session and session['user'] == p['admin_user']):
				post = Posts.query.filter_by(sno=sno).first()
				db.session.delete(post)
				db.session.commit()
		return redirect ('/dashboard')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
		if(request.method=='POST'):
				'''Add entry to the database'''
				name = request.form.get('name')
				email = request.form.get('email')
				phone = request.form.get('phone')
				message = request.form.get('message')
				entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
				db.session.add(entry)
				db.session.commit()
				#mail.send_message('New message from ' + name,
				#                                 sender=email,
				#                                 recipients = [p['gmail-user']],
				#                                 body = message + "\n" + phone
				#                                 )
				flash("Your contact send successfully. You will be contactd soon", "success")
				flash("Lots more to come yet.", "danger")
		return render_template('contact.html',params=p)

if __name__=='__main__':
		app.run(port=5013)

app.run(debug=True)

#cd /etc/apache2/sites-available/
#systemctl reload apache2
#sudo a2ensite cwh
#cd /var/log/apache2
