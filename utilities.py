from math import sqrt


def gcd(a, b): #Finds the GCD of two given numbers
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m): #calculates the inverse modulo function of two numbers
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def isprime(n): #checks if the number is prime or not
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


def converter(msg):
    l = len(msg)
    c = []
    tp = ''
    for i in range(l):
        if(msg[i] == '['):
            continue
        elif(msg[i] == ']'):
            d = int(tp)
            c.append(d)
            tp = ''
            break
        elif(msg[i].isdigit() == True):
            tp = tp+msg[i]
        elif(msg[i] == ','):
            d = int(tp)
            c.append(d)
            tp = ''

    return c