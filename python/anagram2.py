def anagrams_for(word, list_of_words):

    # anagrams have the same letters as the source, but the sequence is not meaningful
    # we will sort both the source and the word to be tested
    word = sorted(word)
    result = []
    for item in list_of_words:
        if sorted(item) == word: result.append(item)
    return result