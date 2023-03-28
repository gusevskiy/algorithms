'''
ОПИСАНИЕ: Завершите функцию scramble(str1, str2), которая возвращает
true, если часть символов str1 можно переставить так, чтобы они
соответствовали str2, в противном случае возвращает false. Примечания:
Будут использоваться только строчные буквы (a-z). Никакие знаки препинания
или цифры не будут включены. Необходимо учитывать производительность.

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

'''


# Мое решение
# def scramble(s1, s2):
#     for i in s2:
#         if i in s1:
#             s1 = s1.replace(i, '', 1)
#             s2 = s2.replace(i, '', 1)
#     if s2 == '':
#         return True
#     return False


def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


#  вот это крутое решение
def scramble_unicode(s1, s2):
    h = [0] * 26
    for c in s1:
        h[ord(c) - 97] += 1
    for c in s2:
        h[ord(c) - 97] -= 1
    return 0 == sum(n < 0 for n in h)


if __name__ == '__main__':
    s1 = "xrohrzmuegsjinnsi"
    # print(s1.count('n'))
    s2 = "rnyonmoyg"

    print(scramble_unicode(s1, s2))