frutas= ["maca","uva","tomate"]
print(frutas)
print(frutas[2])
print(len(frutas))#numero de elementos na lista
frutas.append("cereja")#adiciona elementos
frutas.append("acerola")
print(frutas)
print(len(frutas))
print(frutas[-1])#printa o ultimo item
citricos= ["Limao","Laranja"]
frutas.extend(citricos)#adiciona na lista outra lista
print(frutas)
frutas.remove("maca")#remove um item da lista 
print(frutas)
frutas.pop(1)#remove o respectivo item
print(frutas)
for i in frutas:#printa a lista ate o final
    print(i)
for i in range(len(frutas)):#printa a lista ate o final/2
    print(frutas[i])
frutas.sort()#lista por ordem alfabetica
print(frutas)
numeros=[50,10,40,35,67,83]
numeros.sort()#lista por ordem crescente
print(numeros)
frutas.sort(key=str.lower)#deixa em letra minuscula as frutas
print(frutas)
copiafrutas=frutas#copia a lista, ambas iguais
frutas.append("kiwi")
print(frutas)
print(copiafrutas)
frutas2=frutas.copy()#copia a lista, ambas iguais
frutas3=list(frutas)#copia a lista, ambas iguais
frutas.append("kiwi")
print(frutas)
print(frutas2)
print(frutas3)