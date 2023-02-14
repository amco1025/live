# # 재귀 피보나치
# F(i) = F[i-1] + F[i-2] for i >= 2

# def fibo(n):
#   if n < 2:
#     return n
#   else:
#     return fibo(n-1) + fibo(n-2)

# # Memoization 피보나치
# memo = [0] * (7+1)
# memo[0] = 0
# memo[1] = 1

# def fibo(n):
#   global memo
#   if n >= 2 and memo[n] == 0:
#     memo[n] = (fibo(n-1) + fibo(n-2))
#   return memo[n]

# print(fibo(7))

def fibo(n):
  f = [0] * (n + 1)
  f[0] = 0
  f[1] = 1
  for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]

  return f[n]

print(fibo(7))