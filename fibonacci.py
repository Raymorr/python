def main():
	num = int(input("How many numbers?\n"))
	fib(num)

def fib(num):
	a = 0
	b = 1
	for i in range (num):
		a, b = b, a + b
		print(a, end = ' ')
	print()

if __name__ == "__main__":
	main()	


	
