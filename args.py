def multi(*args):
	res = 1
	for arg in args:
		res *= arg
	return res

a = multi(2, 5, 7, 2, 4)
print(a) # 560


l = [2, 4, 458, 44, 7, 13]

print(l[0], l[1]) 
print(*l)


def mult(a0, *args):
	result = a0 * 2
	for arg in args:
		result *= arg + a0
	return result

b = mult(1, 2, 4, 0)
print(b) # 30


params = {}
params['file'] = "my_file1.txt"
params['mode'] = "w"
params['encoding'] = "utf-8"

with open(**params) as fp:
	fp.write("example string")

print(fp)