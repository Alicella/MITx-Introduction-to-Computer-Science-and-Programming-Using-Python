def genPrimes():
    primes = []
    prime_1 = 1

    while True:
        flag = True

        prime_2 = prime_1 + 1
        if primes:
            for p in primes:
                if prime_2 % p == 0:
                    flag = False
                    break
        if flag:
            next = prime_2
            yield next
            primes.append(prime_2)

        prime_1 = prime_2


pr = genPrimes()
print(pr.__next__())
print(pr.__next__())
print(pr.__next__())
print(pr.__next__())
