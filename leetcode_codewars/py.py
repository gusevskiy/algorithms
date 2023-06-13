


def dict_words(text):
    signs = {
        ord("."): None
        }

    return text.lower().translate(signs).split()


print(dict_words(("  ...  ")))


