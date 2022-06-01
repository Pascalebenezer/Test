# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word_1, word_2):
       # [assignment] Add your code here
    
    if len(word_1) == len(word_2) and sorted(word_1.lower()) == sorted(word_2.lower()):
        return True

    else:
        return False

word_1 = input('Word 1: ')
word_2 = input('Word 2: ')
print("--->", find_anagram(word_1, word_2))