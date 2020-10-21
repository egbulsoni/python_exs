import time

def fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    return fibo(n-1) + fibo (n-2)

def fibo_tail(n, res = 0):
    if (n == 0):
        return res
    elif (n == 1):
        return res + 1
    return fibo_tail(n-1) + fibo_tail(n-2)

def fact(n):
    if (n <= 1):
        return 1
    else:
        return n * fact(n-1)
    
def fact_tail(n, res=1):
    if (n <= 1):
        return res
    else:
        return fact_tail(n-1,res*n)
it = 10
start = time.time()
print(fibo(it))
print('Fibo recursive: {} seconds'.format(time.time() - start))

start = time.time()
print(fibo_tail(it))
print('Fibo tail: {} seconds'.format(time.time() - start))

start = time.time()
print(fact(it))
print('Fact: {} seconds'.format(time.time() - start))

start = time.time()
print(fact_tail(it))
print('Fact tail: {} seconds'.format(time.time() - start))

def maior_elem(ls):
    head, *tail = ls
    if (not tail):
        return head
    return max(head, maior_elem(tail))
    
lista = [1,3,5,2,4]

def soma_elem(ls, s=0):
    head, *tail = ls
    s = s + head
    if not tail:
        return s
    return soma_elem(tail, s)

print(soma_elem(lista))
    
