import requests
url = 'https://api-fxtrade.oanda.com/v1/accounts/12345/orders?instrument=EUR_USD&count=2'
data = '{
  "query": {
    "order": {
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 50,
  "sort": [],
  "facets": {}
}'
headers = {"Accept": "application/json"}
response = requests.post(url, data = data)

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","123","ORDER" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Select qSQL with id=4.
cursor.execute("SELECT qSQL FROM TBLTEST WHERE id = 4")

# Fetch a single row using fetchone() method.
results = cursor.fetchone()

qSQL = results[0]

cursor.execute(qSQL)

# Fetch all the rows in a list of lists.
qSQLresults = cursor.fetchall()
for row in qSQLresults:
    id = row[0]
    order = response.text

    #SQL query to INSERT a record into the table FACTRESTTBL.
    cursor.execute('''INSERT into FACTRESTTBL (id, order)
                  values (%s, %s)''',
                  (id, order))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()