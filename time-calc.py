#Write a function that takes a list of task durations in HH:MM:SS format and returns the total duration.

def time_calc(tasks_duration):
	hour,minute,second = 0, 0, 0
	for duration in tasks_duration:
		items = duration.split(':')
		hour = hour + int(items[0])
		minute = minute + int(items[1])
		second = second + int(items[2])
		minute = minute + second//60
		second = second % 60
		hour = hour + minute//60
		minute = minute%60		
	return [hour, minute, second]	

print(time_calc(["0:35:50","1:56:45"]))			

