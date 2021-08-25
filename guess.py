import random

r = random.randint(1, 100)
while True:
	num = input('guess the number')
	num = int(num)
	if num == r:
		print('bingo!!')
		break
	elif num > r:
		print('greater than the number')
	elif num < r:
		print('less than the number')