import numpy as np  

def print_rb(n=1):
    print(')'*n)

def print_lb(n=1):
    print('('*n)

n = 1
lb= 1
rb= 0
flag= 0

print_lb()
while (flag != 1):
    if (lb == n):
        print_rb()
        break
    elif (lb < n):
        print_lb()
        lb+=1
    while ()