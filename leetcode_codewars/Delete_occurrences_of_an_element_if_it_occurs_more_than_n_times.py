def delete_nth(order, max_e):
    seen = {}
    res = []

    for x in order:
        # если ключа х нет в словаре seen
        if x not in seen:
            # то ключь х = 0
            seen[x] = 0
        else:
            # если ключь х есть в словаре то его значение += 1
            seen[x] += 1

        if seen[x] < max_e:
            res.append(x)
    return res



if __name__ == '__main__':
    print(delete_nth([20,37,20,21], 1))