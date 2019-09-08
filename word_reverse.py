def main():
	string = get_string()
	new_string = reverse(string)
#	print(type(new_string))
	for i in new_string[::-1]:
		print(i, end = " ")
	print()

def get_string():
	return (input("Give me string you want to reverse\n"))

def reverse(st):
	return st.split()

if __name__ == "__main__":
	main()
