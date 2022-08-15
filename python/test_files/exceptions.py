import sys
try:
	print(1/0)
except:
	print(sys.exc_info())
