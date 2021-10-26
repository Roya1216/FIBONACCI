print('WELCOME')
n=int (input("please enter N::"))
fib=[0,1]
for b in range(2,n+1):
    fib.append(fib[b-1]+fib[b-2])
print(fib)