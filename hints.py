myWord = "hello"

choice = input("Type a word: ")

if choice == myWord:
	print:("It's a match")
else:
	print("Not a match")


	# how to check if a letter is in a word

	letter = input("Enter a letter: ")

	if letter in myWord:
		print("Letter is in word")
	else:
		print("Letter is not in word")

	count = 0
	for letter in myWord:
		if letter == choice:
			print (count)
		count += 1

      