#  а каждое последующее число равно сумме двух предыдущих чисел
#  числа фибоначи (рекурсия с мемоизацией)
# def fib(n, dp):
#     if dp[n] == -1:
#         dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
#     return dp[n]


# if __name__ == '__main__':
#     n = int(input())
#     dp = [-1] * (n+1)
#     dp[0] = dp[1] = 1
#     print(fib(n, dp))


# с помощью цикла
n = int(input())
dp = [0]*(n+1)
dp[0]=dp[1]=1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]
    print(dp[i])
print(dp[n])
