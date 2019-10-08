import datetime

def fibonacci1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci1(n-1) + fibonacci1(n-2)

known = { 0:0, 1:1 }
def fibonacci2(n):
    if n in known:
        return known[n]
    result = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = result
    return result

if __name__ == '__main__':
	n = int(input('Please input number: '))
	print(datetime.datetime.now())
	print('\nOne - fibonacci1(%d)=%d\n' % (n, fibonacci1(n)))
	print(datetime.datetime.now())
	print('\nTwo - fibonacci2(%d)=%d\n' % (n, fibonacci2(n)))
	print(datetime.datetime.now())
