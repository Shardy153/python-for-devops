
### Memory Usage Monitor
#Problem: Write a script that checks and prints memory usage of the current system.
#Skills: `psutil`, System Monitoring, Formatting

import psutil
import datetime
import time
import logging

logging.basicConfig(filename="monitor.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
while True:
	
	cpu  = psutil.cpu_percent(interval=1)

	mem = psutil.virtual_memory()

	logging.info(f"CPU: {cpu}")	
	logging.info(f"Memory: {mem.percent}")
	time.sleep(10)

