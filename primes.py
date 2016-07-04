import time

#adding some color
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))

time1 = 0

#waiting for input from user
print(' Hi!')
prGreen("I can calculate all the primes from 0 to n insanely fast")
prCyan("For your own sake, don't use n > 10.000.000 unless you want to wait for a few minutes")
n = int(input(" Enter n ="))

#go!
start = time.time()

#calculation
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

#calculation done! It's time to update time
finish = time.time()
time1 = start - finish

#instant output and small delay with printing all numbers - helpful with huge numbers, like 100.000.000
prGreen('.........\n .......\n .....\n ...\n .\nCalculation complete!!!')
print('Prime numbers found:', len(lst), '\nTime to complete:', time1)
print('Printing results:')
time.sleep(2)

#printing list of all prime numbers in range
prCyan(lst)

#and some fun facts
print('')
print('Prime numbers in range from 0 to', n, ':', len(lst))
print('Sum of all prime numbers in range =', sum(lst))
prGreen("Time to complete, seconds:")
prGreen(time1)
