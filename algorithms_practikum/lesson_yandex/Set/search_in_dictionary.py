'''
Дан словарь из N слов, длинна каждого не превосходит К
В записи каждого из М слов текста (каждое длиной до К)
может быть пропущена одна буква. Для каждого слова сказать, входит ли оно
(возможно, с одной пропущенной буквой), в словарь
'''


def wordsindict(dictionary, text):
    goodwords = set(dictionary)
    for word in dictionary:
        # здесь создается словарь из слов без одной буквы циклом по индексам
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans


if __name__ == '__main__':
    print(wordsindict(set('abc'), 'abcabc'))
