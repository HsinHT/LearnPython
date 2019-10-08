def hanoi(n, x, y, z):
	if n == 1:
		print(x, ' --> ', z)
	else:
		hanoi(n-1, x, z, y)
		hanoi(1, x, y, z)
		hanoi(n-1, y, x, z)

if __name__ == '__main__':
	n = int(input('Please input hanoi towers numbers:'))
	hanoi(n, 'X', 'Y', 'Z')
