frase = input("Informe uma frase: ").upper()
chave = input("Informe a chave: ").upper()

def cifra_frase(frase):
    total_frase = 0
    for i in range(len(frase)):
        letra = frase[i]
        total_frase += ord(letra) - ord('A')
    return total_frase

def cifra_chave(chave):
    total_chave = 0
    for i in range(len(chave)):
        letra = chave[i]
        total_chave += ord(letra) - ord('A')
    return total_chave

# Cifrando a frase e a chave
valor_frase = cifra_frase(frase)
valor_chave = cifra_chave(chave)

# Somando os valores
resultado = (valor_frase + valor_chave) % 26
converter =  chr(66 + (resultado - 1)) if resultado < 26 else 'A'


print("Soma dos valores da frase e da chave:", converter)

        


    
    