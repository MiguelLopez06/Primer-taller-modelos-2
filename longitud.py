def longitud (x):
	if x<=9:
	   return 0
	else:
	   return 1 + longitud(x/10)
print(longitud(3244123423)+1)
