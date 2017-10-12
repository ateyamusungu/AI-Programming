import matplotlib.pyplot as plt

file = open('alice.txt','r')

words_bag = dict()
for line in file:
    for word in line.split():
        if word in words_bag:
            words_bag[word] = words_bag[word]+1
        else:
            words_bag[word] = 1


frequent_words = dict()

for a,b in words_bag.items():
    if b > 100:
        frequent_words[a] = b



plt.bar(range(len(frequent_words)), frequent_words.values())
plt.xticks(range(len(frequent_words)), frequent_words.keys(),rotation=-90)
plt.title('Bar Histogram of most frequent words')
plt.xlabel('Words')
plt.ylabel('Frequency of words')
plt.show()
