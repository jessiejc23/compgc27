from flask import Flask, render_template, session, make_response, request, jsonify
app = Flask(__name__)

import pyaudio
import wave
import numpy as np
import pymysql.cursors
import plotly as py
from plotly.graph_objs import *
import pandas as pd
from ac_model import ac_classifier


app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['SECRET_KEY'] = 'JeCheJiXiYuHe'


hostname = 'localhost'
username = 'root'
password = 'xxx' #root for jimmy's laptop
database = 'accent_classifier'
port = 9092 #3306 for jimmy's laptop


@app.route('/', methods=["GET"])
def index():
  return render_template('homepage.html')

@app.route('/about.html', methods=["GET"])
def render_about():
	return render_template('about.html')

@app.route('/instructions.html', methods=["GET"])
def render_instructions():
	return render_template('instructions.html')

@app.route('/record.html', methods=["GET"])
def record():
	return render_template('record.html')

@app.route('/wikipedia.html')
def wikipedia():
	return render_template('wikipedia.html')

@app.route('/restaurants.html')
def restaurants():
	return render_template('restaurants.html')

def retrieve_database_country(number):
	conn = pymysql.connect( host=hostname, port = port, user=username, passwd=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor )
	cur = conn.cursor()
	query = ("SELECT Country FROM apiLookup "
		     "WHERE number = '%d'" % (number))
	cur.execute(query)
	
	for item in cur:
		country = item['Country']
	conn.close()

	return country


@app.route('/record-audio/', methods=["GET","POST"])
def record_audio():
	CHUNK = 1024
	WIDTH = 2
	CHANNELS = 2
	RATE = 44100
	FORMAT = pyaudio.paInt16
	RECORD_SECONDS = 2
	WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	wav_file = []

	stream = p.open(format=p.get_format_from_width(WIDTH),
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                output=True,
	                frames_per_buffer=CHUNK)

	print("* recording")
	t = 0
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    #print (i)
	    #print i, for 3 seconds i prints from 0 to 128, so total 129 bytes. 129 divide by 3 = 43..? 
	    if (i%42) == 0:
	        print('%d seconds left' %(23-t))
	        t+=1
	    data = stream.read(CHUNK, exception_on_overflow = False)
	    #print(type(data))
	    wav_file.append(data)
	    
	print("* done")
	stream.stop_stream()
	stream.close()
	p.terminate()

	#the following converts a list to a byte object
	#byte = b''.join(wav_file) 

	#the following saves the audio file but our project doesn't require this step.
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(wav_file))
	wf.close()

	#run model to output a result 

	#country = retrieve_database_country(number)
	#add how to retrieve mfcc from deep learning model
	ac = ac_classifier()
	number, mfcc = ac.predict('/Users/jessietan/Desktop/COMPGC27/Final_Project_Codes/output.wav') 
	#need to modify the templates bit because it is not saved in templates folder
	country = retrieve_database_country(number)
	#print(country)
	session['mfcc'] = mfcc.tolist()
	session['number'] = int(number)

	return render_template("result.html", country = country, number = session['number'])

def retrieve_database_api(number):
	conn = pymysql.connect( host=hostname, port = port, user=username, passwd=password, db=database, cursorclass=pymysql.cursors.DictCursor  )
	cur = conn.cursor()
	query = ("SELECT Country_wikipedia, Country_restaurants FROM apiLookup "
		     "WHERE number = '%d'" % (number))
	cur.execute(query)
	for item in cur.fetchall():
		wikipedia = item['Country_wikipedia']
		cuisine = item['Country_restaurants']
	conn.close()

	return wikipedia, cuisine

@app.route('/go-to-select/', methods=["GET","POST"])
def go_to_select():
	return render_template('select.html', data=[{'country':'USA', 'value':0}, {'country':'UK', 'value':1}, {'country':'Spain', 'value':2}, {'country':'France','value':3},
		{'country':'Russia', 'value':4},{'country':'Saudi Arabia', 'value':5}, {'country':'China', 'value':6},{'country':'Saudi Arabia', 'value':7}, {'country':'Japan', 'value':8}, {'country':'Others', 'value':9} ])

@app.route('/insert-results/', methods=["GET","POST"])
def insert_results():
	conn = pymysql.connect( host=hostname, port = port, user=username, passwd=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor )
	cur = conn.cursor()
	value = session['number']
	mfcc = session ['mfcc']
	query = (" INSERT INTO `audioFiles` (`number`, `mfcc`) VALUES ('%d', hextoraw(%s))" % (number, mfcc))
	cur.execute(query)
	conn.close()
	country = retrieve_database_country (number)
	wikipedia, cuisine =retrieve_database_api (number)
	return render_template("checkresult.html", country = country, wikipedia = wikipedia, cuisine = cuisine)

@app.route('/_array2python', methods=["GET", "POST"])
def array2python():
	session['number'] = request.form.get('comp_select')
	insert_results()
	return make_response(jsonify("do nothing for now")), 204

@app.route('/plot-graph/', methods = ["POST"])
def plot_graph():
	number = session['number']
	conn = pymysql.connect( host=hostname, port = 9092, user=username, passwd=password, db=database )
	cur = conn.cursor()
	cur.execute( "SELECT * FROM total "
				"WHERE number = '%d'" % (number))

		    #for Country in cur.fetchall() :
		       # print (Country)
	total = cur.fetchall()
	total = np.asarray(total).reshape(18, )
	total = total[1:]
		    

	cur.execute( "SELECT * FROM graduate " 
		    	 "WHERE number = '%d'" % (number))

		    #for Country in cur.fetchall() :
		       # print (Country)
	grad = cur.fetchall()
	grad = np.asarray(grad).reshape(18, )
	grad= grad[1:]
		    

	cur.execute( "SELECT * FROM undergraduate " 
		    	 "WHERE number = '%d'" % (number))

		    #for Country in cur.fetchall() :
		       # print (Country)
	undergrad = cur.fetchall()
	undergrad = np.asarray(undergrad).reshape(18, )
	undergrad= undergrad[1:]

	years=['2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000']
	years =np.array(years)

	time_series= {'year':years,'total':total,'undergrad':undergrad,'grad':grad}
	df = pd.DataFrame(data=time_series)

	x = years
	trace0 = Scatter(
		x = x,
		y = df['total'],
		mode = 'total',
		name = 'total'
	)

	trace1 = Scatter(
		x = x,
		y = df['undergrad'],
		mode = 'undergraduate',
		name = 'undergraduate'
	)

	trace2 = Scatter(
		x = x,
		y = df['grad'],
		mode = 'graduate',
		name = 'graduate'
	)
			
	layout = Layout (
		title = 'Year vs Student Stats',
		xaxis = XAxis(title = 'Year'),
		yaxis = YAxis(title= 'Number of Students in UCL')

	)
			
	data = [trace0, trace1, trace2]
	fig = Figure(data= data, layout = layout)
			
	py.offline.plot(fig,filename="{{url_for('templates', filename='graph.html')}}", auto_open=False)
	conn.close()
	return render_template('checkresult_graph.html')

if __name__ == '__main__':
  app.run(debug=True)