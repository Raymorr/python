def main():
	winner = 0
	while winner == 0:
		first = input("The first, print Rock, Papper or Scissors\n")
		second= input("The second, print Rock, Papper or Scissosrs\n")
		if (first != 'Rock' and first != 'Papper' and first != 'Scissors') or (second != 'Rock' and second != 'Papper' and second != 'Scissors') :
			print('Error\n\n')
		else:
			winner = compare(first, second)
			if(winner == 1): print('The first won')
			elif(winner == 2): print('The second won')
			else :
				end = input('Dead heat, try one more or print Stop\n')
				if(end == 'Stop'): winner = -1


def compare(first, second):
	if(first == "Rock"):
		f = 1
	elif (first == "Papper"):
		f = 2
	else:
		 f = 3

	if(second == "Rock"):
		s = 1
	elif (second == "Papper"):
		s = 2
	else:
		 s = 3	 

	if f - s == 0:
		return 0
	elif f - s == -2 or f - s == 1:
		return 1
	elif f - s == -1 or f - s == 2:
		return 2
	return 0

if __name__ == "__main__" :
	main()
