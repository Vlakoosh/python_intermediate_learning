"""Find palindromes"""
import load_dictionary
word_list = load_dictionary.load("./dictionaries/words.txt")
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\n Number of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
