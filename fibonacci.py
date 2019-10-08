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
	n = 20
	print(datetime.datetime.now())
	print('One - fibonacci1(%d)=%d' % (n, fibonacci1(n)))
	print(datetime.datetime.now())
	print('Two - fibonacci2(%d)=%d' % (n, fibonacci2(n)))
	print(datetime.datetime.now())
