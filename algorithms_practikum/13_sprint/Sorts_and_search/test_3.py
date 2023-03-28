def count_Down(start, indent=1):
    print('-'*indent, 'UP:', start)
    if start == 0:
        # Здесь рекурсивный вызов 'countDown' прекратился, сначала
        #  печатается эта строчка, потом все, что было накоплено в стеке...
        print('-'*indent, 'DOWN:', start)
    else:
        # Рекурсивный вызов 'countDown'
        count_Down(start - 1, indent + 1)
        # Вызов 'countDown' не дает функции print выполнится
        # и накапливает (откладывает) ее исполнение в стеке
        print('-'*indent, 'DOWN:', start)

count_Down(5)