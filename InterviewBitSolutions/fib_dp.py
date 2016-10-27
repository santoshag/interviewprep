def fibo(n, memo):
  if n <= 1: return n
  # If we have processed this function before, return the result from the last time.
  if memo[n] != 0: return memo[n];
  # Otherwise calculate the result and remember it.

  memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
  print n, n -1, n-2, memo
  return memo[n]

fibo(5, [0] * 6)
