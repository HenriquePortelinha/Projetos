import random
import string
import time

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = " ".join(random.choice(caracteres) for i in range(8))
    return senha.replace(" ", "")


print(f"-" * 30)
print(f"Gerador de senhas")
print(f"-" * 30)
print(f"Vamos criar uma senha aleatória? S/N")
escolha = input("Digite S para sim ou N para não: ").upper()
if escolha == "S":
    print(f"-" * 30)
    time.sleep(1)
    print(f"Gerando senha...")
    time.sleep(2)
    print(f"-" * 30)
    print(f"Sua nova senha é: {gerar_senha()}")
else:
    print(f"-" * 30)
    print(f"Até mais")
    print(f"-" * 30)

