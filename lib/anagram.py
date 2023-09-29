# your code goes here!

class Anagram:
    def __init__(self, word_to_check):
        self.word_to_check = word_to_check

    def match(self, list_of_words):
        anagrams_found = []
        for word in list_of_words:
            if ("".join(sorted(self.word_to_check)) == "".join(sorted(word))):
                anagrams_found.append(word)
        return anagrams_found if len(anagrams_found) > 0 else []
