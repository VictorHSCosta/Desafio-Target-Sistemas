def quantidadeDeLetras(texto , letra):
    contador = 0

    #faz com que ele identifique independente se a letra é maiuscula ou minuscula
    texto = texto.lower()
    letra = letra.lower()

    for i in texto:
        if i == letra:
            contador += 1
    return contador

def main():
    texto = input('Digite um texto: ')
    letra = input('Digite uma letra: ')
    print(f'A letra {letra} aparece {quantidadeDeLetras(texto, letra)} vezes no texto')

if __name__ == '__main__':
    main()