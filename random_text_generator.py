import random
import string

# wordlengths:       1 2 3 4 5 6 7
# their frequencies: 1 2 3 4 3 2 1
wordlength_frequences = [1] + [2] * 2 + [3] * 3 + [4] * 4 + [5] * 3 + [6] * 2 + [7]

vowels = "aeiou"

def generate_n_words(n):
	for i in range(n):
		wordlength = random.choice(wordlength_frequences)
		word = ""
		for letter in range(wordlength):
			letter = random.choice(string.ascii_lowercase)
			word += letter
		if word_contains_vowels(word):
			yield word
		else: 
			continue		

def word_contains_vowels(word):
	for letter in word:
		if letter in vowels:
			return True
	return False	
	
def main(): 
	words_to_generate = int(input("How many words do you need, playa?\n"))
	with open("random_words.txt", "a+") as output_file: # open for reading and writing, create is doesn't exist and append
		new_line = ((' ').join(word for word in generate_n_words(words_to_generate)))
		output_file.write(new_line + "\n")

if __name__ == "__main__":
    main()
