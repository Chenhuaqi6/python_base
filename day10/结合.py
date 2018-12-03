def isprime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
            break
    else:
        return True
        
def prime_m2n(m,n):
    L = []
    for x in range(m,n):
        if isprime(x):
            L.append(x)
    return L

def primes(n):
    return prime_m2n(0, n)
L = primes(100)
print(L)
S = primes(200)
print(sum(S))