
def f1():
	x = 98
	def f2(x=x):
		print(x)
	f2()
f1()
# should work as python 3.5
# otherwise, not... that is - python prior 2.2 dies..
#
