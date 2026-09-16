sentence = input("Enter a sentence: ")
vowel_count = 0

for character in sentence:
	if character == ".":
		break
	if character.lower() in "aeiou":
		vowel_count += 1

print(vowel_count)