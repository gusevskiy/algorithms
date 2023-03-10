'''
Например, 'heart' и 'earth' - это анаграммы. Как и строки 'python' и 'typhon'.
 Для простоты будем полагать, что обе заданные строки одной длины и составлены
из набора символов в 26 букв в нижнем регистре.
Наша цель - написать булеву функцию, принимающую две строки и возвращающую
ответ на вопрос, являются ли они анаграммами.

Решение 1: Метки
Первое решение задачи про анаграмму будет проверять, входит ли каждый из
символов первой строки во вторую. Если все символы будут “отмечены”, то строки
являются анаграммами. “Пометка” символа будет выполняться с помощью замены
его на специальное значение Python None. Однако, поскольку строки в Python
 иммутабельны, первым шагом обработки станет конвертирование второй строки
 в список. Каждый символ из первой может быть сверен с элементами списка и,
 если будет найден, отмечен оговоренной заменой.
'''


def anagramSolution1(s1,s2):
    """Метод перебором всех букв и их сравнение"""
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def anagramSolution2(s1,s2):
    """Метод с сортировкой и сравнением"""
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagramSolution4(s1,s2):
    """ Через unicode считает количество букв в строке и если совпадают True"""
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


if __name__ == '__main__':
    # print(anagramSolution1('abcdi','dcba'))
    # print(anagramSolution2('abcd','dcba'))
    print(anagramSolution4('abcii','bciia'))