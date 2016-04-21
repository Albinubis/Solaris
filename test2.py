import math
wert=input("Geben sie einen Wert ein: ")
g=0
for i in range(1, wert+1):
	g=round(math.pow(math.sin(i)*2,3))+i
	a=""
	if g >= 0:
		for c in range(1, int(g+1)):
			a=a+"#"
		print a
