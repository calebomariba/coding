import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)


# TODO: Add your function generate_password below
def generate_password():
	return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    selected_words=random.sample(word_list,3)
    password= "".join(selected_words)
    return password


# Now we test the function
print(generate_password())