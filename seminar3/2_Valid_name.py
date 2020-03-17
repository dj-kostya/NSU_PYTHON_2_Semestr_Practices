def is_word(word: str):
    if not word.istitle():
        raise ValueError
    if len(word) in (0, 1):
        raise ValueError
    if len(word) == 2 and word[-1] == '.':
        return False
    if word.find('.') != -1:
        raise ValueError
    return True


def validate_name(string: str):
    words = string.split()
    if len(words) > 3:
        return False
    type_words = []
    for word in words:
        try:
            type_words.append(is_word(word))
        except ValueError:
            return False
    if not type_words[0]:
        if type_words[1] and len(words) == 2:
            return True
        if not type_words[1] and type_words[2]:
            return True
    else:
        if type_words[1] and type_words[2]:
            return True
        elif not type_words[1] and type_words[2]:
            return True
    return False

# validate_name('H Wells') -> False
# validate_name('H. George Wells') -> True
