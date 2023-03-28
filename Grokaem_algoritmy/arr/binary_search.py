num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37,
           38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

str_arr = ['Adam', 'Adrian', 'Agnes', 'Alba', 'Albin', 'Alexande', 'Alfred', 'Algot', 'Ali', 'Alice', 'Alicia', 'Alma', 'Alva', 'Alvar', 'Alve', 'Alvin', 'Amelia', 'Anton', 'Aron', 'Arvid', 'Aston', 'Astrid', 'August', 'Axel', 'Ayla', 'Benjamin', 'Bianca', 'Bonnie', 'Carl', 'Casper', 'Celine', 'Charlie', 'Clara', 'Cleo', 'Colin', 'Cornelia', 'Daniel', 'Dante', 'Ebba', 'Ebbe', 'Edith', 'Edvin', 'Elias', 'Elin', 'Elina', 'Elis', 'Elise', 'Ella', 'Ellen', 'Ellie', 'Elliot', 'Elsa', 'Elsie', 'Elton', 'Elvin', 'Elvira', 'Emil', 'Emilia', 'Emma', 'Erik', 'Ester', 'Felix', 'Filip', 'Filippa', 'Folke', 'Frank', 'Frans', 'Freja', 'Gabriel', 'Gustav', 'Hailey', 'Hanna', 'Harry', 'Hedda', 'Hedvig', 'Henry', 'Hilda', 'Himla', 'Hjalmar', 'Hugo', 'Ida', 'Idun', 'Ilse', 'Ines', 'Ingrid', 'Iris', 'Isabella', 'Isabelle', 'Isak', 'Ivar', 'Jack', 'Jacob', 'Jasmine', 'Joel', 'Joline', 'Jonathan', 'Josef', 'Julia', 'Julian', 'Julie', 'Juni', 'Kian', 'Leah', 'Leia', 'Leo', 'Leon', 'Levi', 'Liam', 'Lilly', 'Linnea', 'Liv', 'Livia', 'Loke', 'Louie', 'Lova', 'Love', 'Lovis', 'Lovisa', 'Lucas', 'Ludvig', 'Luna', 'Lykke', 'Maja', 'Majken', 'Malte', 'Maria', 'Maryam', 'Matteo', 'Max', 'Meja', 'Melina', 'Melissa', 'Melker', 'Melvin', 'Mila', 'Millie', 'Milo', 'Milton', 'Mira', 'Moa', 'Mohammed', 'Molly', 'Nellie', 'Nicholas', 'Nils', 'Noah', 'Noel', 'Nora', 'Nova', 'Oliver', 'Olivia', 'Olle', 'Omar', 'Oscar', 'Otis', 'Otto', 'Ronja', 'Ruth', 'Saga', 'Sally', 'Sam', 'Samuel', 'Sara', 'Selma', 'Sigge', 'Signe', 'Sigrid', 'Siri', 'Sixten', 'Sofia', 'Stella', 'Stina', 'Svante', 'Svea', 'Tage', 'Ted', 'Thea', 'Theo', 'Theodor', 'Tilde', 'Ture', 'Tuva', 'Tyra', 'Vera', 'Vidar', 'Vide', 'Viggo', 'Viktor', 'Vilgot', 'Vincent', 'Walter', 'Wilda', 'Wilhelm', 'William', 'Wilma', 'Wilmer', 'Zoe', 'rta']

# Работает только по отсортированному типу данных

# бинарным поиском стр 27
def binary_search(ar, item):
    low = 0
    high = len(ar)-1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2  # деление по модулю чтоб не создовать float
        gees = ar[mid]
        if gees == item:
            return f'Элемент {mid} кол. оп {count}'
        if gees > item:
            high = mid - 1
        else:
            low = mid + 1
    return f'Элемент {None} кол. оп {count}'


if __name__ == '__main__':
    print(binary_search(str_arr, 'Adrian'))
    print(len(str_arr))


