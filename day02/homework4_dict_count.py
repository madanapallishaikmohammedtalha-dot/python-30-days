#dict count 
list_of_words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

words_count = {}

def word_count(words):
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

word_count(list_of_words)

print(words_count)