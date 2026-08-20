from collections import OrderedDict

n = int(input())
word_counts = OrderedDict()

for i in range(n):

    word = input()  
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
print(*(word_counts.values()))