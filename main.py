def to_cyrillic(name):
    custom_translation = {
        "A": "А",
        "a": "а",
        "B": "Б",
        "b": "б",
        "C": "К",
        "c": "к",
        "D": "Д",
        "d": "д",
        "E": "Э",
        "e": "э",
        "F": "Ф",
        "f": "ф",
        "G": "Г",
        "g": "г",
        "H": "Х",
        "h": "х",
        "I": "И",
        "i": "и",
        "J": "Ж",
        "j": "ж",
        "K": "К",
        "k": "к",
        "L": "Л",
        "l": "л",
        "M": "М",
        "m": "м",
        "N": "Н",
        "n": "н",
        "O": "O",
        "o": "o",
        "P": "П",
        "p": "п",
        "Q": "К",
        "q": "к",
        "R": "Р",
        "r": "р",
        "S": "С",
        "s": "с",
        "T": "Т",
        "t": "т",
        "U": "У",
        "u": "у",
        "V": "В",
        "v": "в",
        "W": "В",
        "w": "в",
        "X": "Кс",
        "x": "кс",
        "Y": "Й",
        "y": "й",
        "Z": "З",
        "z": "з"

    }

    translation_table = str.maketrans(custom_translation)

    cyrillic_name = name.translate(translation_table)
    return cyrillic_name


user_input = input("Enter a name(without diacritics!): ")

name_in_cyrillic = to_cyrillic(user_input)
print("Your name in Cyrillic:", name_in_cyrillic)
