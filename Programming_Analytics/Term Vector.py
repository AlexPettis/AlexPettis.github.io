import string

filename = input("Enter filename: ")
infile = open(filename, 'r')

text = infile.read().lower()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
word_counts = {}


for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts_list = list(word_counts)
new_word_counts_list = sorted(word_counts_list)

print("There are " + str(len(new_word_counts_list)) + " unique terms.")

for word in new_word_counts_list:
    print(word_counts[word], word)

infile.close()
