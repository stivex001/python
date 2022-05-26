# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter First word: ")
    anagram = input("Enter secong word: ")

    if sorted(word)== sorted(anagram):
        return True
    else:
        return False

print(find_anagram("word", "anagram"))

