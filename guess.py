import random
start = input('set up the random value and its range as starting: ')
end = input('set up the random value and its the range as ending: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1 
	num = input('guess the number: ')
	num = int(num)
	if num == r:
		print('bingo!!')
		print('you have counted', count, 'time(s)')
		break
	elif num > r:
		print('greater than the number')
	elif num < r:
		print('less than the number')
	print('you have counted', count, 'time(s)')