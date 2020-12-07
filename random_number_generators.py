import random


#functions that generate a random string, consisting of a certain number of integers within a certain range
#this was used to create a slug for a user when the user was created
#both versions achieve the same result

#version 1
def gen_random_number():
	number = range(8)
	var = ''
	for c in number:
		var = var + str(random.randint(0, 9))
	return var

#version 2
def gen_random_number():
	return(''.join(str(random.randint(0, 9)) for i in range(8)))
