"""
Prime Number

"""
import sys

def main():
	
	names = []
	name = 'primes'
	for _ in range(1, 51):
		names.append(name + str(_) + '.txt')
	
	contents = []
	
	for element in names:
		with open(element) as f:
			for line in f:
				line = line.split()
				for word in line:
					if word.isdigit():
						contents.append(word)

	for _ in contents:
		with open('primes_list_50m.txt', 'w') as prime_file:
			prime_file.write(_)
				
if __name__ == '__main__':
	main()
