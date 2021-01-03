#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request,json
import os ,subprocess
import os,csv,pathlib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler import BackgroundScheduler
import atexit

app = Flask(__name__)
app.secret_key = 'super-secret-key'

path = pathlib.Path(__file__).parent.absolute()
path = "/home/praveen/Downloads/cleanblog"
filename = "aqi_temp_7days.csv"
filepath = os.path.join(path, filename)


local_server = True
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:India123*@localhost/codingthunder"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = p['prod_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

scheduler = BackgroundScheduler()
#scheduler = BlockingScheduler()

# Database table properties

class airquality(db.Model):
	sno = db.Column(db.Integer,primary_key=True)
	city = db.Column(db.String(50), nullable=False)
	feeddate = db.Column(db.String(50), nullable=False)
	actualcity = db.Column(db.String(50), nullable=False)
	hour = db.Column(db.Integer,nullable=False)
	aqi = db.Column(db.Decimal(10,1) , nullable=False)
	temp = db.Column(db.Decimal(10,1) , nullable=False)
	co = db.Column(db.Decimal(10,1) , nullable=False)
	dew = db.Column(db.Decimal(10,1) , nullable=False)
	humidity = db.Column(db.Decimal(10,1) , nullable=False)
	no2 = db.Column(db.Decimal(10,1) , nullable=False)
	o3 = db.Column(db.Decimal(10,1) , nullable=False)
	p = db.Column(db.Decimal(10,1) , nullable=False)
	pm10 = db.Column(db.Decimal(10,1) , nullable=False)
	pm25 = db.Column(db.Decimal(10,1) , nullable=False)
	w = db.Column(db.Decimal(10,1) , nullable=False)

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
		with open(abs_file_path,'a') as f3:
			writer=csv.writer(f3)
			writer.writerow(city_aqi_temp_date_time)

def SaveInSQL():
    city_to_use='Pune'
    data1=getDataAqi(city_to_use)
    if data1['status']=="ok":
        city=city_to_use
        feeddate= datetime.now().strftime("%d/%m/%Y")
        actualcity=data1['data']['city']['name']
        hour = datetime.now().strftime("%H")
        aqi=data1['data']['aqi']
        temp=data1['data']['iaqi']['t']['v']
        co = data1['data']['iaqi']['co']['v']
        dew = data1['data']['iaqi']['dew']['v']
        humidity = data1['data']['iaqi']['h']['v']
        no2 = data1['data']['iaqi']['no2']['v']
        o3 = data1['data']['iaqi']['o3']['v']
        p = data1['data']['iaqi']['p']['v']
        pm10 = data1['data']['iaqi']['pm10']['v']
        pm25 = data1['data']['iaqi']['pm25']['v']
        w = data1['data']['iaqi']['w']['v']
        post = airquality(city=city, feeddate=feeddate, actualcity=actualcity,
                             hour=hour, aqi=aqi, temp=temp, co=co, dew=dew, humidity=humidity, no2=no2, o3=o3, p=p, pm10=pm10, pm25=pm25, w=w)
        db.session.add(post)
        db.session.commit()
citi='Pune'
responses=getDataAqi(citi)
#print(responses['data']['iaqi'])

scheduler.add_job(func=SaveInSQL, trigger="interval", seconds=20)
#scheduler.add_job(SaveInSQL, 'interval', seconds=10)
scheduler.start()
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())