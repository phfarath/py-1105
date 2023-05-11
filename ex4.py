import re
try:
    print("digite seu nome: ")
    nome=input()
    if re.search("\d", nome):
        erro="o nome so pode conter letras"
    print("digite seu telefone: ")
    cel=input()
    if re.search("\d{10}{11}",cel):
        erro="o telefone deve conter ate 11 digitos"
    print(f'nome:{nome}\ncel:{cel}\n')
except ValueError:
    print(erro)  
finally:
    print("obrigado!")