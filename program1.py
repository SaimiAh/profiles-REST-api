def sieve_of_eratosthenes(start, end):
    prime = [True for _ in range(end + 1)]
    prime[0] = prime[1] = False

    p = 2

    while p * p <= end:
        if prime[p]:
            for i in range(p * p, end + 1, p):
                prime[i] = False
        p += 1

    for num in range(max(2, start), end + 1):
        if prime[num]:
            print(num, end=' ')

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

print("Prime numbers between {} and {}:".format(start, end))
sieve_of_eratosthenes(start, end)
