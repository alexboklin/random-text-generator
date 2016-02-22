import random
import string

wordlength_frequences = [1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7]   	# wordlengths:       1 2 3 4 5 6 7
																# their frequencies: 1 2 3 4 3 2 1       

def generate_n_words(n):
	for i in range(n):
		wordlength = random.choice(wordlength_frequences)
		word = ""
		for letter in range(wordlength):
			letter = random.choice(string.ascii_lowercase)
			word += letter

		yield word	

def main(): 
	words_to_generate = int(input("How many words do you need, playa?\n"))
	print((' ').join(word for word in generate_n_words(words_to_generate)))

if __name__ == "__main__":
    main()  
