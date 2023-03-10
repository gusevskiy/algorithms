# Хеш функции представляют собой функцию, которая получает строку и возвращает число
# они также называются ассоциативными массивами, словарями, хеш карты или просто хеши
# в python это словари

voted = {}
def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        voted[name] = True
        print('let them vote')

