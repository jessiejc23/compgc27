hostname = 'localhost'
username = 'root'
password = 'xxx'
database = 'accent_classifier'


def retrieve(number, conn):

	'''search database number column with the number
	return corresponding wikipedia and restaurant'''
	cur = conn.cursor()
	query = ("SELECT Country_wikipedia, Country_restaurants FROM api_lookup "
		     "WHERE number = '%d'" % (number))
	cur.execute(query)
	for Country_wikipedia, Country_restaurants in cur.fetchall():
	#	print (Country_wikipedia, Country_restaurants)
		
		wikipedia = Country_wikipedia
		cuisine = Country_restaurants

	return wikipedia, cuisine




print ("Using mysql.connector…")
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, port = 9092, user=username, passwd=password, db=database )
wikipedia, cuisine = retrieve(0, myConnection )
print("hey")
print(wikipedia)
print(cuisine)
myConnection.close()