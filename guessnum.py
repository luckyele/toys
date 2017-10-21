import random

a = random.randint(1,9)
b = input("Input one number:")
print "\n"

while 1:
	if b > a:
		print "Big"
	elif b < a:
		print "litte"
	elif b == a:
		print "You win"
		break
	b = input("Input one number:\n")


