a=int(input("Digite um número inteiro: "))
b=int(input("Digite outro número inteiro: "))
c=int(input("Digite mais um número inteiro: "))
d=int(input("Digite o último número inteiro: "))
media=(a+b+c+d)/4
print("A média:", media)
if media>=6:
    print("Aprovado")
elif media>=5:
    print("Recuperação")
else:
    print("Reprovado")