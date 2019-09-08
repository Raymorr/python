import random	
#import pdb
def main():
#	pdb.set_trace()
	tries = 0
	fl = 1
	true_number = random.randint(1, 9)
	f_st = input("Guess the number between 1 and 9\n")
	if(not f_st.isdigit()) :
		print ('Error')
		return	
	else:
		num = int(f_st)
		if(num > 9 or num < 1) :
			print ('Error')
			return

	while fl == 1:
		tries = tries + 1
		if num > true_number:
			print("Too high, print Stop if you want to stop guessing")
			while True:
				num = new_st()
				fl = check(num)
				if(fl == 2): continue
				if(fl == 1): break
				break

		elif num < true_number:
			print("Too low, print Stop if you want to stop guessing")
			while True:
				num = new_st()
				fl = check(num)
				if(fl == 2): continue
				if(fl == 1): break
				break
		
		else:
			print("You won!")
			print("Total numbers of attempts - %d" %tries)
			fl = 0

def isint(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def new_st():
	a = input()
	if(a == 'Stop') : return -1
	elif (not a.isdigit()) : return -2
	elif (int(a) < 1 or int(a) > 9) : return -2
	else: return int(a)

def check(n):
	if(n == -1) : return 0
	elif(n == -2) :
		print("Error input, try again")
		return 2
	else : return 1
			 
if __name__ == "__main__":
	main()	
