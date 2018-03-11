def isPrime(a):
    divider = 2
    while a % divider != 0:
        divider += 1

    if divider == a:
            print(a, ' - простое число')
    else:
            print(a, '- составное число')


isPrime(3)
isPrime(5)
isPrime(7)
isPrime(10)
isPrime(18)
isPrime(25)
