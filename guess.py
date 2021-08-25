import random

r = random.randint(1, 100)
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