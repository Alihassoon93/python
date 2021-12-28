def reverse_file(filename):
	'''Overwrite given file with its contents line-by-line reversed.'''
	
	S = ArrayStack() # alternatively u can also use list in python
	original = open(filename)
	for line in original:
		S.push(line.rstrip('\n')) # for list use append instead of push
	original.close()

	output = open(filename, 'w')
	while not S.is_empty(): # for list use len(list) != 0
		output.write(S.pop() + '\n')
	output.close()
