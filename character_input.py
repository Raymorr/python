import datetime
def main():
	name = get_name()
	age = get_age()
	year = get_year(age)
	
	if year == 0:
		print ("Error!")
	else:
		print (name, 'you will be 100 years old in the year ' + str(year))


def get_name():
	return (input('What is your name?\n'))


def get_age():
	return (int(input('How old are you?\n')))

	
def get_year(age):
	if age  >= 100 or age <= 0:
		return 0
	else:
		year = datetime.datetime.now().year
		return (year + (100 - age))


if __name__ == "__main__":
	main()
