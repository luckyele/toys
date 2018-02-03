from random import randint
import cProfile

# get a integer number K
def read():
	return int(input())

# generate K integers
def generate_int(k):
	aint = []

	while True:
		if len(aint) == k:
			break
		a = randint(1, k)
		if a not in aint:
			aint.append(a)
			print(a)
	return aint 	

# save
def save(a):
	f = open('data.txt', 'w')
	for item in a:
		f.write(str(item))
		f.write('\n')
	f.close()	
	print("total write %d items to files."%len(a))

# main
def main():
	k = read()	
	save(generate_int(k))

if __name__ == "__main__":
	cProfile.run('main()')

	
