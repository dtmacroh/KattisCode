iter = int(eval(input("")))
count = 0
while count < iter:

	word = input("")
	if len(word) > 10:
		print(word[0] + str((len(word)-2)) + word [len(word)-1])
	else:
		print(word)
	count = count+1
	