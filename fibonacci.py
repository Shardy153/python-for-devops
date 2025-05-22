#Fibonacci Generator
def fibbonaci_generator(n):
	series = [0,1]

	for i in range(2,n):
		series.append(series[i-1] + series[i-2])
	
	return series


result = fibbonaci_generator(7)
print(result)
