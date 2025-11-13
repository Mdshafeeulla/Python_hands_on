# Dictionary Comprehension
#
# Challenge
# Given a list of words, create a dictionary where keys are words and values are the counts of vowels in each word.
#
# Skills Required
# 1.Dictionary comprehension syntax
# 2.String iteration
# 3.Conditional counting
# 4.Character classification

def vowels_given(words):
    len_of_vowels = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        length = 0
        for char in word:
            if char.lower() in vowels:
                length += 1

        len_of_vowels[word] = length
    print(len_of_vowels)

vowels_given(words = ['My','Name','is','Mohammed'])
