def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
    return ans


def fib(n):
    d = {1:1, 2:2}
    return(fib_efficient(n, d))


print(fib(900))
