digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6] # длины слов «ноль», «один»,...


def card_strength(card): # ключ сравнения
    return digit_lengths[card]


def is_first_card_weaker(card_1, card_2):  # функция-компаратор
    return card_1 < card_2


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


if __name__ == '__main__':
    cards = [3, 7, 9, 2, 3]
    print(insertion_sort_by_key(cards, is_first_card_weaker))
    # print(card_strength(3))