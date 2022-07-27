def main():
    s = "programacao"
    f = "aprovado"
    c = input('Entre com a letra para a alocação:')

    # quantas letras existem e em que posições?
    lst = []
    for pos, char in enumerate(s):
        if char == c:
            lst.append(pos)

    print("posições onde foi encontrada a letra 'a'", lst)
    # vamos imprimir a letra usando a posicao 2 da lista
    lposi = lst[1]
    x = 0
    for l in s:
        if x == lposi:
            print(f)
        else:
            print(l)
        x += 1

if __name__ == '__main__':
    main()


# EXPLICANDO O ALGORITIMO

'''

    Na primeira linha ele define a função main, que é função principal do código que está sendo chamda na linhan 24
    
    NA linha 2 e 3 ele define as palavras que vão fazer 'intersecção', onde a primeira letra da segunda deve estar presente na frase 1
    
    Na linha 3 ele pede em qual letra você deseja inserir a alocação ("cruzar" as palavras), que consequentemente deve ser a letra a 
    para que não haja erro no programa, ou então um cruzamento assimétrico
    
    Na linha 8 ele defini um loop que vai percorrer a primeira palavra, alocando uma varíavel para cada letra dela no percorrimento
    e também sua numeração a partir da função enumerate
    
    Na linha 9 ele definiu uma verificação, onde caso a letra que ele escolheu na linha 3 esteja presente na palavra a sua posição
    será salva em uma lista, que foi gerada na linha 7 fora do loop,
    
    Com as posições onde ele pode inserir a segunda palavra e cruzar com a primeira salva, ele as mostra na linha 12
    
    Como nesse caso a letra escolhida aparece mais de uma vez ele defini a segunda vez em que ela parece, na linha 14
    
    Na linha 15 ele inicializa uma variável x, que serivrá como contador e consequentemente medidor de posição.
    
    Na linha 16 ele defini um loop, que irá percorrer a primeira palavra
    
    Na linha 17 ele executa uma verificação, em que se a posição da letra que ele está mostrando na palavra for a mesma
    que ele definiu anteriormente como ponto de encontro e alocou na variável c, O programa não mostra a letra na palavra,
    mas sim a palavra 2 inteira, que tem como primeira letra a letra que ele deixou de mostrar. Assim não deixando a palavra 1
    com uma letra falatando;
    
    Na linha 19 e 20 ele mostra a letra da primeira palavra na vertical caso a condição de igualdade das posições não seja estabelecida
    
    Na linha 21 ele incrementa o contador x a cada vez que o loop se repetir, para assim saber em que posição da palavra ele está.
    
'''