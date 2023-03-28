'''
a=5
b=6
c=10
for i in range(n):
   for j in range(n):
      x = i * i
      y = j * j
      z = i * j
for k in range(n):
   w = a*k + 45
   v = b*b
d = 33
'''
import time

'''Число операций присваивания представляет собой сумму из четырёх слагаемых. 
Первое - константа 3, отражающая три присваивания в начале фрагмента. 
Второе - 3n2
, поскольку три присваивания выполняются n2
 раз внутри вложенной итерации. Третье - 2n
 - два присваивания, повторяющиеся n
 раз. Наконец, четвёртое слагаемое - константа 1, 
 представляющая последний оператор присваивания. 
 Всё вместе это даёт T(n)=3+3n2+2n+1=3n2+2n+4
. Глядя на степени, мы легко можем заметить, что слагаемое n2
 будет доминантой, и следовательно, этот фрагмент кода является O(n2)
. Обратите внимание, что прочие слагаемые (так же, как и коэффициенты) 
при возрастании n можно проигнорировать.'''

def search_min_On(n):
    start = time.time()
    n_min = n[0]
    for i in n:
        if i < n_min:
            n_min = i
    end = time.time()
    return n_min, end - start


def search_min_On2(n):
    start = time.time()
    n_min = n[0]
    for i in n:
        for x in range(i):
            if x < i:
                x = n_min
    end = time.time()
    return n_min, end - start



if __name__ == '__main__':
    n = [2, 56, 4, 65, 2, 6]
    print("Min is %d required %10.7f seconds"%search_min_On(n))
    print("Min is %d required %10.7f seconds"%search_min_On2(n))