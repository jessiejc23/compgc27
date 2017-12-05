hostname = 'localhost'
username = 'root'
password = 'xxx'
database = 'accent_classifier'


def retrieve(number, conn):

	'''search database number column with the number
	return corresponding wikipedia and restaurant'''
	cur = conn.cursor()

    cur.execute( "SELECT 2016-total FROM uclStudentStats WHERE Country =" + number)

    print (2016-total)



print ("Using mysql.connector…")
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, port = 9092, user=username, passwd=password, db=database )
retrieve("UK", myConnection )
myConnection.close()