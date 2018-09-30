#imports for DataStax Cassandra driver and sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import SimpleStatement
import sys
import csv
import pandas as pd

#reading hostname, username, and password from the command line; defining Cassandra keyspace as as variable.
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
keyspace="<keyspace>"

chunksize = 1000
filename  = 'data.csv'

#adding hostname to an array, setting up auth, and connecting to Cassandra
nodes = []
nodes.append(hostname)
auth_provider = PlainTextAuthProvider(username=username, password=password)
ssl_opts = {}
cluster = Cluster(nodes,auth_provider=auth_provider,ssl_options=ssl_opts)
session = cluster.connect(keyspace)

#if you don't have headers in the first row of the csv then give header=None inside read_csv
#otherwise it won't read the first row
for chunk in pd.read_csv(filename, chunksize=chunksize,iterator=True):
	for index, row in chunk.iterrows():		
                print index
		#sample
    		key = str(row['id'])
    		user_id = str(row['user_id'])
    		data = str(row['data'])

		#preparing and executing my INSERT statement
		strCQL = "INSERT INTO data (id,user_id,data) VALUES (?,?,?)"
		pStatement = session.prepare(strCQL)
		session.execute(pStatement,[key,user_id,data])

#closing my connection
session.shutdown()
