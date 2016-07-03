import time

def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))

time1 = 0
print(' Hi!')
prGreen("I can calculate all the primes from 0 to n insanely fast")
n = int(input(" Enter n ="))

start = time.time()

a = list(range(n+1))
a[1] = 0
lst = [1]

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in list(range(i, n+1, i)):
            a[j] = 0
    i += 1

finish = time.time()
time1 = start - finish

prGreen('.........\n .......\n .....\n ...\n .\nCalculation complete!!!')
print('Prime numbers found:', len(lst), '\nTime to complete:', time1)
print('Printing results:')
time.sleep(2)

prCyan(lst)
print('')
print('Prime numbers in range from 0 to', n, ':', len(lst))
print('Sum of all prime numbers in range =', sum(lst))
prGreen("Time to complete, seconds:")
prGreen(time1)
