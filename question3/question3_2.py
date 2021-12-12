def factorize(n):
    result = 1
    while n > 0:
        result = result*n
        n -= 1
    return result

def layer(n):
    if n == 1: return [1]
    result = [1]*n
    for i in range(1, n-1):
        result[i] = int(factorize(n-1) /(factorize(i)*factorize(n-1 -i)))
    return result

print(layer(4))