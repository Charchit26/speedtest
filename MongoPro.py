from pymongo import MongoClient
import datetime

# import socket to get hostname of machine
import socket

# Python program to calculate RTT

import time
import requests
from time import sleep
# Function to calculate the RTT
def RTT(url, result):

	# time when the signal is sent
	t1 = time.time()

	r = requests.get(url)
	#sleep(0.8)
	# time when acknowledgement of signal 
	# is received
	t2 = time.time()

	# total time taken
	tim = str(t2-t1)

	print("Time in seconds :" + tim)
	result.append(tim)

# driver program 
# url address

urls = ["http://192.168.0.1","https://stackoverflow.com","http://127.0.0.1/","http://facebook.com"]
result = []
i=0
while(i<len(urls)):
	try:
		RTT(urls[i], result)
	except Exception as e:
		print("SOme Exception occured for the url --> "+urls[i])
		print(e)
		result.append("null")
	i+=1
	
new_dict=dict(zip(urls,result));

print(new_dict)
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("127.0.0.1:27017")
db=client.speedTest
collection=db.hpseCollection
post = {"author": socket.gethostname(),"testResult": new_dict,"date": datetime.datetime.utcnow()}

post_id=collection.insert(post,check_keys=False)
print(post_id)