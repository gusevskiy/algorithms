def moving_average(timeseries, K):
    result = []  # Пустой массив.
    for begin_index in range(0, len(timeseries)-K+1):
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = round((current_sum / K), 2)
        result.append(current_avg)
    return result


def optimization_m_a(timeseries, K):
    result = []
    curent_sum = sum(timeseries[0:K])
    result.append(curent_sum / K)
    for i in range(0, len(timeseries) - K):
        curent_sum -= timeseries[i]
        curent_sum += timeseries[i+K]
        curent_avg = round((curent_sum / K), 2)
        result.append(curent_avg)
    return result


arr = [4, 3, 8, 1, 5, 6, 3]

print(moving_average(arr, 3))  # -> [5.0, 4.0, 4.67, 4.0]

print(optimization_m_a(arr, 3))  # -> [5.0, 4.0, 4.67, 4.0, 4.67]

