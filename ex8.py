lista=[]
negativos=0
pares=0
num1=1
while num1 !=0:
    print("digite um numero inteiro:")
    num1=int(input())
    lista.append(num1)
    resto=num1%2
    if num1<0:
        negativos+=1
    if resto==0:
        pares+=1
lista.sort()
lista.remove()
print(lista)