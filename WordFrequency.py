infile = open("AI.txt", "r")

word_frequency = dict()

for line in infile:
    for word in line.split():
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1


print(word_frequency)
