def verificar_letra_a(texto):
    
    ocorrencias = texto.lower().count('a')
    
    
    if ocorrencias > 0:
        print(f"A letra 'a' aparece {ocorrencias} vez(es) na frase.")
    else:
        print("A letra 'a' não está presente na frase.")


texto_usuario = input("Digite uma frase: ")


verificar_letra_a(texto_usuario)