import time

#adding some color
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))

time1 = 0

#waiting for input from user
print(' Hi!')
prGreen("I can calculate all the primes from 0 to n insanely fast")
prCyan("For your own sake, don't use n > 10.000.000 unless you want to wait for a few minutes")
n = int(input(" Enter n =")) #спрашивает число n

#go!
start = time.time()

#calculation
a = list(range(n+1)) #добавляет список всех натуральных чисел от 0 до n+1, первое число a[0] = 0
a[1] = 0 #заменяет второе число было 1 на 0 чтобы не прошло if выражение
# lst = [1] !!! тут на самом деле нужно убрать 1 так, как 1 не является простым числом
lst = [] # убрал 1 из список простых чисел

i = 2 # начинаем с a[2] = 0 так как a[0] и a[1] = 0
while i <= n:
    if a[i] != 0:  # исключаем  a[0] и a[1]
        lst.append(a[i])
        for j in list(range(i, n+1, i)): # тут создается список всех чисел при умножении на i до n+1
            a[j] = 0 # заменяет эти числа  на 0 чтобы не прошли if выражение
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
prCyan(lst) # вазврашает список всех простых чисел до n

#and some fun facts
print('')
print('Prime numbers in range from 0 to', n, ':', len(lst))
print('Sum of all prime numbers in range =', sum(lst))
prGreen("Time to complete, seconds:")
prGreen(time1)
