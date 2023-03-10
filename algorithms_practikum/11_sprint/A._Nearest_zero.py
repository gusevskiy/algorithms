
# House
# Длина улицы = n * x
# x = длинна участка
# x >= 0

# def distance_to_zero(distance):
#     zero = 0
#     ds = []
#     for index, data in enumerate(distance):
#         if data == 0:
#             zero = index
#     for i, y in enumerate(distance):
#         ds.append(zero - i)
#         # print(i)
#
#     return ds

# def distance(distance):
#     lastsym = distance[0]
#     ds = []
#     for i in range(len(distance)):
#         if distance[i] == lastsym:
#             ds.append(lastsym)
#         elif distance[i] != lastsym:
#             ds.append(i)
#     return ds

# def long_street(s):
#     def distance_to_zero(distance):
#         distance_back = distance[::-1]
#         ds = []
#         for index in range(len(distance)):
#             ds.append(min(distance[index], distance_back[index]))
#         # print(ds)
#         return ''.join(ds)
#
#     ss = s.split('0')
#     dad = []
#     for i in ss:
#         dad.append(i)
#     print('dad', dad)
#
#     index_dad = []
#     for i in dad:
#         for x in i:
#             index_dad.append(x)
#     print('index_dad', index_dad)
#     return index_dad


def long_street(numbers, street):
    rer = street.split('0')
    print(rer)


def distance_to_zero(number, distance):
    distance_back = distance[::-1]
    ds = []
    for index in range(number):
        ds.append(min(distance[index], distance_back[index]))
    return ''.join(ds)




if __name__ == '__main__':
    distance_1 = '1234'
    street = '043104515'
    str = 'how are you?'
    # print(len(street))
    # print(distance_to_zero(4, distance_1))
    # print(distance(street))
    print(long_street(9, street))