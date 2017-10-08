# Python program to calculate RTT

import time
import requests
from time import sleep
# Function to calculate the RTT
def RTT(url):

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

# driver program 
# url address

urls = ["http://192.168.0.1","https://stackoverflow.com","http://127.0.0.1/","http://facebook.com"]
i=0
while(i<len(urls)):
	try:
		RTT(urls[i])
	except Exception as e:
		print("SOme Exception occured for the url --> "+urls[i])
		print(e)
	i+=1
