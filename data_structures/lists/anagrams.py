# Given a list of string words, group the words that are anagrams of each other

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Expected Output: [["eat", "tea", "ate"], ["nat, "tan"], "bat"]

def grouping_anagrams(words):

    anagram_dictionary = {}

    for word in words:
        sorted_word = str(sorted(word))

        if sorted_word not in anagram_dictionary:
            anagram_dictionary[sorted_word] = []

        anagram_dictionary[sorted_word].append(word)

    sorted_list = list(anagram_dictionary.values())
    return sorted_list

print(grouping_anagrams(words))
