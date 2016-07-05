def primes(n):
    a = list(range(n+1)) #generate all whole numbers from 0 to n
    a[1] = 0 # replace 1 in a list by 0 so it doesn't pass the if statement
    lst = [] #empty list where the prime numbers go

    i = 2 # the first 2 numbers in a are 0 and 0, so we start by the 3 a[2]
    while i <= n:
        t = a[i]
        if t != 0: # if the number from the a list is not 0
            lst.append(t) #then append it to the primes numbers list
            lst_div = list(range(i, n+1, i)) #create all numbers that can divide t
            for j in lst_div:
                a[j] = 0 #make those numbers zeros so they don't pass the if statement
        i += 1
    print (lst) # shouldn't it be return(lst) ?
