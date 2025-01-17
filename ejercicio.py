
x = 0

print("dame un numero ")
num = input('Numero: ')
res = int(num)


if res == 0:
    print("todo numero multiplicado por 0 es 0 ")
else :
    n = 1
    while n <=10:
        result = res * n

        print("la multiplicacion de {} * {} ={}".format(num,n,result))

        n+=1
    
  

