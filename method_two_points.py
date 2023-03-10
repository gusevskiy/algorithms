# Удалить дубли методом двух указателей
# [0, 0, 0, 1, 1, 1, 2, 2, 3, 3]

def remove_dublicates(numb):
    first_point, second_point = 0, 0
    
    while second_point < len(numb):
        while second_point < len(numb) -1 and numb[second_point] == numb[second_point + 1]:
            second_point += 1
            
        numb[first_point] = numb[second_point]
        first_point += 1
        second_point += 1
        
    return numb[:first_point]


print(remove_dublicates([0, 0, 0, 1, 1, 1, 2, 1, 3, 3]))
