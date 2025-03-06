alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"

escolha = int(input("\n== SELECIONE UMA OPÇÃO: ==\n1 - Cifrar mensagem\n2 - Decifrar mensagem\n: "))

if escolha == 1:
    
    print("\nNão use acentos ou caracteres especiais!\n")
    frase = input("Informe uma frase: ")
    chave = input("Informe a chave: ")
    chave = chave.replace(' ', '')

    def cifrar(frase, chave):
        resultado = ''
        tamanho_chave = len(chave)
        j = 0 # índice da chave

        # cifrar letra por letra
        for i in range(len(frase)):
            letra = frase[i]
            
            if letra in alfabeto_maiusculo:
                letra_frase = alfabeto_maiusculo.index(letra) 
                letra_chave = chave[j % tamanho_chave] 
                posicao_letra_chave = alfabeto_maiusculo.index(letra_chave) 
                
                valor_cifrado = (letra_frase + posicao_letra_chave) % 26
                resultado += alfabeto_maiusculo[valor_cifrado]
                j += 1  
                
            elif letra in alfabeto_minusculo:
                letra_frase = alfabeto_minusculo.index(letra)
                letra_chave = chave[j % tamanho_chave]
                posicao_letra_chave = alfabeto_minusculo.index(letra_chave)
                valor_cifrado = (letra_frase + posicao_letra_chave) % 26
                resultado += alfabeto_minusculo[valor_cifrado]
                j += 1  
                
            else:
                resultado += letra  # mantém acentuações e caracteres especiais

        return resultado

    frase_cifrada = cifrar(frase, chave)
    print("\nFrase cifrada:", frase_cifrada)
    
elif escolha == 2:
    print("\nNão use acentos ou caracteres especiais!\n")
    frase = input("Informe a frase: ")
    chave = input("Informe a chave: ")
    chave = chave.replace(" ", "")

    def decifrar(frase, chave):
        resultado = ''
        tamanho_chave = len(chave)
        j = 0 # índice da chave

        # cifrar letra por letra
        for i in range(len(frase)):
            letra = frase[i]
            
            if letra in alfabeto_maiusculo:
                letra_frase = alfabeto_maiusculo.index(letra) 
                letra_chave = chave[j % tamanho_chave] 
                posicao_letra_chave = alfabeto_maiusculo.index(letra_chave) 
                
                valor_decifrado = (letra_frase - posicao_letra_chave) % 26
                resultado += alfabeto_maiusculo[valor_decifrado]
                j += 1  
                
            elif letra in alfabeto_minusculo:
                letra_frase = alfabeto_minusculo.index(letra)
                letra_chave = chave[j % tamanho_chave]
                posicao_letra_chave = alfabeto_minusculo.index(letra_chave)
                valor_decifrado = (letra_frase - posicao_letra_chave) % 26
                resultado += alfabeto_minusculo[valor_decifrado]
                j += 1  
                
            else:
                resultado += letra  # mantém acentuações e caracteres especiais

        return resultado

    frase_decifrada = decifrar(frase, chave)
    print("\nFrase decifrada:", frase_decifrada)