from itertools import permutations 
import pprint
import enchant
import sys


def power_set(input):
    # returns a list of all subsets of the list input
    if (len(input) == 0):
        return [[]]
    else:
        main_subset = [ ]
        for small_subset in power_set(input[1:]):
            main_subset += [small_subset]
            main_subset += [[input[0]] + small_subset]
        return main_subset


def permutation(list):
	new_list = []
	for i in range(len(list)):
		perm = permutations(list[i])
		for i in perm:
			new_list.append(i)

	return new_list


def main():

	test_str = sys.argv[1]
	list = power_set(test_str)

	new_list = []

	#remove where size is greater than 2 or less than 7
	for i in range(len(list)):
		if(len(list[i]) > 2 and len(list[i]) < 7):
			new_list.append(list[i])

	itertools_list = permutation(new_list)

	perm_list = []

	for perm in itertools_list:
		perm_list.append(''.join(perm))

	
	valid_words = []
	d = enchant.Dict("en_US")
	for i in perm_list:
		if(d.check(i)):
			valid_words.append(i)
	
	#get rid of repeats
	real_valid_words = []
	for word in valid_words:
		if(word not in real_valid_words):
			real_valid_words.append(word)

	real_valid_words.sort()
	pprint.pprint(real_valid_words)
	print(len(real_valid_words))


main()


