try:
    print("digite dois numeros inteiros")
    num1=int(input())
    if not type(num1)is int:
        raise ValueError
    num2=int(input())
    if not type(num2)is int:
        raise ValueError
    if num2<=0:
        #raise- print do erro
        raise ZeroDivisionError
    print(f"divisao: {num1/num2}")
#except- erro é trocado por frase 
except ValueError:
    print("Erro: Somente numeros inteiros sao permitidos")
except ZeroDivisionError:
    print("Erro : Segundo numero deve ser maior do que zero")
#finally- print independente do erro ou nao
finally:
    print("Obrigado por utilizar nosso programa ")