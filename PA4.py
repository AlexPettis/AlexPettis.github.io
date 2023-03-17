f = open("moxy.csv", 'r')
total = 0
for line in f:
    word_list = line.split()
    for word in word_list:
        number = int(word)
        total += number
print("The sum is", total)
