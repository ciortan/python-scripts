import urllib.request
import subprocess
import time
from datetime import datetime

stop_jira = ['service', 'jira', 'stop'];
start_jira = ['service', 'jira', 'start'];
try:
	status_page = urllib.request.urlopen('https://jira.allot.com/status').read()
	text = status_page.decode("utf-8")
	if "state" in text and "RUNNING" in text:
		print (datetime.now()," ok")
	else:
		print (datetime.now()," error")
		subprocess.call(stop_jira, shell=False)
		time.sleep(10)
		subprocess.call(start_jira, shell=False)
	pass
except Exception as e:
	print (datetime.now()," error")
	subprocess.call(stop_jira, shell=False)
	time.sleep (10)
	subprocess.call(start_jira, shell=False)
	pass