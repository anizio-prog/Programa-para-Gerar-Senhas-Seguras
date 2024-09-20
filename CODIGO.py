# Programa-para-Gerar-Senhas-Seguras
# O programa tem como objetivo criar senhas fortes e aleatórias, que são difíceis de serem adivinhadas ou quebradas. Ele permite que o usuário escolha o tamanho da senha, garantindo que ela atenda a requisitos de segurança.

import random
import string

def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha (mínimo 12): "))
    if tamanho < 12:
        print("A senha deve ter pelo menos 12 caracteres.")
    else:
        senha_segurada = gerar_senha(tamanho)
        print(f"Sua senha segura gerada: {senha_segurada}")
