import math

d=input("Tag: ")
m=x=input("Monat: ")
m=m-2
if m < 1:
	m=m+12
j=input("Jahr: ")
if m < 11:
	c=math.floor(j/100)
	y=math.floor(j-c*100)
else:
	c=math.floor((j-1)/100)
	y=math.floor((j-1)-c*100)

w=(d+math.floor(2.6*m-0.2)+y+math.floor(y/4)+math.floor(c/4)-2*c)%7
print "Tag: "
if w == 0:
	print "Sonntag"
if w == 1: 
	print "Montag"
if w == 2: 
	print "Dienstag"
if w == 3: 
	print "Mittwoch"
if w == 4: 
	print "Donnerstag"
if w == 5: 
	print "Freitag"
if w == 6: 
	print "Samstag"
