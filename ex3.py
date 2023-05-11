import re
erro=""
try:
    print("digite seu nome")
    nome=input()
    if re.search("\d", nome):
        erro="nomes nao podem conter numeros "
        raise ValueError
    print("digite seu cep(somente digitos)")
    cep=input()
    if not re.search("\d{8}", cep) or len(cep)>8:
        erro="o cep deve conter 8 digitos "
        raise ValueError
    print(f"nome:{nome}\ncep:{cep}\n")
except ValueError:
    print(erro)
finally:
    print("fim do programa")