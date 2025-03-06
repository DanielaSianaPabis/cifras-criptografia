alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"

resposta = int(input("\n== SELECIONE UMA OPÇÃO: ==\n1 - Cifrar mensagem\n2 - Decifrar mensagem\n: "))

if resposta == 1:
    frase = input("\nInforme uma frase (SEM ACENTOS E CARACTERES ESPECIAIS): ")
    deslocamento = int(input("Informe o deslocamento: "))

    frase_cifrada = ''
    for i in range(len(frase)):
        letra = frase[i]
        if letra in alfabeto_maiusculo:
            cifrar_letra = (alfabeto_maiusculo.index(letra) + deslocamento) % 26
            frase_cifrada += alfabeto_maiusculo[cifrar_letra] 
        elif letra in alfabeto_minusculo:
            cifrar_letra = (alfabeto_minusculo.index(letra) + deslocamento) % 26
            frase_cifrada += alfabeto_minusculo[cifrar_letra] 
        else:
            frase_cifrada += letra
        
    print(f"\nFrase cifrada: {frase_cifrada}")

elif resposta == 2:
    frase = input("\nInforme uma frase cifrada (SEM ACENTOS E CARACTERES ESPECIAIS): ")

    for deslocamento in range(1,26):
        frase_decifrada = ''
        for i in range(len(frase)):
            letra = frase[i]
            if letra in alfabeto_maiusculo:
                decifrar_letra = (alfabeto_maiusculo.index(letra) - deslocamento) % 26
                frase_decifrada += alfabeto_maiusculo[decifrar_letra] 
            elif letra in alfabeto_minusculo:
                decifrar_letra = (alfabeto_minusculo.index(letra) - deslocamento) % 26
                frase_decifrada += alfabeto_minusculo[decifrar_letra] 
            else:
                frase_decifrada += letra
            
        print(f"\nDeslocamento de {deslocamento}: {frase_decifrada}")

else:
    print("Erro! Opção inválida.")


