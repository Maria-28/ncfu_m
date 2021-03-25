b1 = int(input('Ввод числа b1:'))
a1 = int(input('Ввод числа a1:'))
b2 = int(input('Ввод числа b2:'))
a2 = int(input('Ввод числа a2:'))
c1 = (a1+b1)% 10
c2 = a2 + b2 + (a1+b1)//10
print (c2,c1)