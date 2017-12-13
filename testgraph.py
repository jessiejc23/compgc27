#https://stackoverflow.com/questions/36262748/python-save-plotly-plot-to-local-file-and-insert-into-html
#https://stackoverflow.com/questions/34327282/is-there-anyway-to-make-plot-ly-graphs-html-standalones
#https://stackoverflow.com/questions/37912260/plotting-graph-using-python-and-dispaying-it-using-html


import plotly as py
from plotly.graph_objs import *
import numpy as np
import pandas as pd
import pymysql.cursors


hostname = 'localhost'
username = 'root'
password = 'xxx'
database = 'accent_classifier'

# Simple routine to run a query on a database and print the results:
def doQuery(number, conn ) :
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
	
    py.offline.plot(fig,filename='/Users/jessietan/Desktop/COMPGC27/Final_Project_Codes/templates/8.html')

print ("Using mysql.connector…")
import mysql.connector
myConnection = pymysql.connect( host=hostname, port = 9092, user=username, passwd=password, db=database )
doQuery(8, myConnection )
myConnection.close()