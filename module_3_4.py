def single_root_words(root_words, *other_words ):
    same_words = []
    for word in other_words:
        if word.lower() in root_words.lower() or root_words.lower() in word.lower():
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
