class Palavra:

    def __init__(self, palavra, tamanho_do_lado):
        self.palavra = palavra
        self.matriz = []  # Vetor que vai armazenar a posição Aij de cada letra na matriz e a letra correspondente a posição
        self.caca_palavras = []  # Matriz quadrada que vai conter o caça-palavras completo
        self.tamanho_do_lado_tabuleiro = tamanho_do_lado

    def inserir_palavra(self, palavra, direcao, sentido):  # DIREÇÃO ////  1 = HORIZONTAL   2 = VERTICAL    #SENTIDO   ///   1 = NORMAL  2 = CONTRÁRIO
        from random import randint
        lista = []

        if sentido == 1:
            i = randint(0, self.tamanho_do_lado_tabuleiro - len(palavra))
            j = randint(0, self.tamanho_do_lado_tabuleiro - len(palavra))

        else:  # Tratamento para que não existam letras fora do range da matriz
            i = randint(0 + len(palavra), self.tamanho_do_lado_tabuleiro - 1)
            j = randint(0 + len(palavra), self.tamanho_do_lado_tabuleiro - 1)

        if len(self.matriz) == 0:  # Caso em que se insere a primeira palavra, onde defini o par ordenado de maneira aleatoria para primeira letra

            if i > self.tamanho_do_lado_tabuleiro - 1 or j > self.tamanho_do_lado_tabuleiro - 1:
                deslocar = True
            else:
                deslocar = False

            for letra in palavra.upper().replace(' ', ''):

                if deslocar:
                    if direcao == 1:
                        lista.append(i)
                        lista.append(j - 1)
                        lista.append(letra)

                    elif direcao == 2:
                        lista.append(i - 1)
                        lista.append(j)
                        lista.append(letra)

                if not deslocar:
                    lista.append(i)
                    lista.append(j)
                    lista.append(letra)  # Processo de adicionar a posição e a letra no vetor

                self.matriz.append(lista[:])
                lista.clear()

                if direcao == 1:  # Para direção horizontal irei incrementar a coluna, para que cada letra seja adicionada na mesma linha

                    if sentido == 1:
                        j += 1             # Para o sentido, caso ele seja contrário irei decrementar, para que assim ele percorra da direita para esquerda
                    elif sentido == 2:
                        j -= 1

                elif direcao == 2:  # Para direção Vertical irei incrementar a Linha, para que cada letra seja adicionada na mesma coluna
                    if sentido == 1:
                        i += 1
                    elif sentido == 2:
                        i -= 1

            return

        else:               # Para os casos onde já existam letras inseridas na matriz
            cont = 0
            while True:
                cont += 1
                if cont > 5000:
                    print('Não existe posição possível para essa palavra')
                    break
                if sentido == 1:
                    i = randint(0, self.tamanho_do_lado_tabuleiro - len(palavra))
                    j = randint(0, self.tamanho_do_lado_tabuleiro - len(palavra))       # Botei no “loop” para caso haja conflito de posicoes ele gerar uma nova posicao para testagem

                else:  # Tratamento para que não existam letras fora do range da matriz
                    i = randint(0 + len(palavra), self.tamanho_do_lado_tabuleiro - 1)
                    j = randint(0 + len(palavra), self.tamanho_do_lado_tabuleiro - 1)

                inserir = self.percorrer_espacos(palavra, direcao, sentido, i, j)

                if i > self.tamanho_do_lado_tabuleiro - 1 or j > self.tamanho_do_lado_tabuleiro - 1:
                    deslocar = True
                else:
                    deslocar = False

                if inserir == 'livre':
                    for letra in palavra.upper().replace(' ', ''):
                        if deslocar:
                            if direcao == 1:
                                lista.append(i)
                                lista.append(j - 1)
                                lista.append(letra)

                            elif direcao == 2:
                                lista.append(i - 1)
                                lista.append(j)
                                lista.append(letra)

                        if not deslocar:
                            lista.append(i)
                            lista.append(j)
                            lista.append(letra)  # Processo de adicionar a posição e a letra no vetor

                        self.matriz.append(lista[:])
                        lista.clear()

                        if direcao == 1:  # Para direção horizontal irei incrementar a coluna, para que cada letra seja adicionada na mesma linha

                            if sentido == 1:
                                j += 1  # Para o sentido, caso ele seja contrário irei decrementar, para que assim ele percorra da direita para esquerda
                            elif sentido == 2:
                                j -= 1

                        elif direcao == 2:  # Para direção Vertical irei incrementar a Linha, para que cada letra seja adicionada na mesma coluna
                            if sentido == 1:
                                i += 1
                            elif sentido == 2:
                                i -= 1

                    return

    def posicao_ocupada(self, linha, coluna):  # Retorna um bool correspondente a disponibilidade da posição IxJ
        for letra in self.matriz:
            if letra[0] == linha and letra[1] == coluna:  # A função percorre todas as posições i e j, e caso tenha alguma posição IxJ já ocupada ele retorna o valor falso.
                return True

        return False

    def percorrer_espacos(self, palavra, direcao, sentido, i, j):   # Função que será utilizada para percorrer os espaços e identificar sobreposição de letras, as impedindo
        for letra in palavra:
            for item in self.matriz:
                if i == item[0] and j == item[1] and letra != item[2]:
                    return 'erro'

            if direcao == 1:  # Para direção horizontal irei incrementar a coluna, para que cada letra seja adicionada na mesma linha

                if sentido == 1:
                    j += 1  # Para o sentido, caso ele seja contrário irei decrementar, para que assim ele percorra da direita para esquerda
                elif sentido == 2:
                    j -= 1

            elif direcao == 2:  # Para direção Vertical irei incrementar a Linha, para que cada letra seja adicionada na mesma coluna
                if sentido == 1:
                    i += 1
                elif sentido == 2:
                    i -= 1

        return 'livre'

    def tratando_tabuleiro(self):
        from random import choice
        linha = []
        for a in range(self.tamanho_do_lado_tabuleiro):
            for u in range(self.tamanho_do_lado_tabuleiro):    # Aqui eu inseri as linhas no tabuleiro, mas ainda preenchidas com x
                linha.append('x')

                if len(linha) == self.tamanho_do_lado_tabuleiro:
                    self.caca_palavras.append(linha[:])
                    linha.clear()


        for cont, linha in enumerate(self.caca_palavras):      # Aqui eu inseri as minhas letras da matriz nas suas respectivas posições no tabuleiro
            for it in self.matriz:
                if it[0] == cont:
                    try:
                        linha[it[1]] = it[2]
                    except:
                        pass

        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        for c1, lista in enumerate(self.caca_palavras):         # Aqui eu adicionei letras aleatorias as posições que não estavam ocupadas
            for c2, item in enumerate(lista):
                if item == 'x':
                    self.caca_palavras[c1][c2] = choice(letras)

    def mostrar_tabuleiro(self):
        print('\033[47m\033[1;30m                   CAÇA-PALAVRAS                     \033[m')
        print()
        for c, linha in enumerate(self.caca_palavras):
            print(f'\033[1;97m{c:2})\033[m', end='   ')
            for coluna in linha:                                # Aqui eu printei o tabuleiro a partir das linhas organizadas anteriormente
                print(coluna, end='  ')
            print()

    def mostrar_tabuleiro_colorido(self):
        print('\033[47m\033[1;30m                     RESOLUÇÃO                       \033[m')
        print()
        for c, linha in enumerate(self.caca_palavras):
            print(f'\033[1;97m{c:2})\033[m', end='   ')          # Aqui eu gerei um print com as palavras destacadas, para caso o jogador não ache e queira saber as posições
            for c2, coluna in enumerate(linha):                  # Para isso eu fiz uma verificação, onde se a letra que ele for imprimir estiver na matriz de letras inseridas
                                                                 # ele vai dar um flag e definir a variavel colorir com true.
                colorir = False
                for item in self.matriz:
                    if c == item[0] and c2 == item[1]:
                        colorir = True

                if not colorir:
                    print(coluna, end='  ')
                if colorir:
                    print(f'\033[32m{coluna}\033[m', end='  ')


            print()

    def main(self):
        from time import sleep
        from random import randint      # Defini a função principal da minha classe com a ordem que eu quero que o jogo tome

        palavras = []

        print('\033[1;97m-' * 15)
        print('\033[33;1m CAÇA PALAVRAS')
        print('\033[1;97m-\033[m' * 15)
        print('\033[1;97mVocê irá digitar as palavras que deseja e o jogo ira as embaralhar no tabuleiro.\n\033[1;91mIsso será feito '
              'de maneira aleátoria, tanto em direção quanto em sentido!!!\033[m')

        while True:
            try:
                qtd_palavras = int(input('\n\033[97mQuantas palavras você deseja inserir? \033[m'))
                if 0 < qtd_palavras <= self.tamanho_do_lado_tabuleiro // 2:
                    break
            except ValueError:
                print(f'Digite um valor válido, que esteja entre 0 e {self.tamanho_do_lado_tabuleiro // 2}:')

            print(f'Digite um valor que esteja entre 0 e {self.tamanho_do_lado_tabuleiro // 2} para não sobrecarregar o tabuleiro')

        for i in range(qtd_palavras):
            while len(palavras) != qtd_palavras:
                try:
                    palavra = input(f'Digite a {i + 1} palavra: ')
                    palavras.append(palavra.strip().upper())

                    direcao = randint(1, 2)
                    sentido = randint(1, 2)

                    jogo.inserir_palavra(palavra, direcao, sentido)
                    break

                except ValueError:
                    print('Digite a palavra')

        print()
        print('\033[31m\033[47m             DIFICULDADE              \033[m')

        print('\033[1;97mVocê pode escolher 4 níveis de dificuldade\033[m:'
              '\n\033[1;32mNível 1\033[m: Vôce terá \033[97m3 minutos\033[m para achar as palavras' 
              '\n\033[32mNível 2\033[m: Você terá \033[97m2 minutos\033[m para achar as palavras'
              '\n\033[33mNível 3\033[m: Você terá \033[97m1 minuto\033[m para achar as palavras'
              '\n\033[31mNível 4\033[m: Você terá \033[97m30 segundos\033[m para achar as palavras'
              '\n\033[1;31mNível 5\033[m: Você é um Deus, e terá \033[97m10 segundos\033[m para achar as palavras')

        while True:
            try:
                dificuldade = int(input('\nDigite o nível de dificuldade desejado: '))     # Quando esse tempo passar o usuário irá ver o tabuleiro com as palavras que ele escolheu marcadas
                if 0 < dificuldade <= 5:
                    break
            except ValueError:
                print('Digite um valor válido')
            print('Digite um valor válido')

        print()
        jogo.tratando_tabuleiro()
        jogo.mostrar_tabuleiro()

        print('\n\033[1;32mBOA SORTE NA BUSCA!!!')

        print(f'\n \033[97mCONTADOR\033[m:')

        from tqdm import tqdm
        if dificuldade == 1:                    # Gerando o contador de acordo com a dificuldade
            for _ in tqdm(range(1, 181)):
                sleep(0.95)

        elif dificuldade == 2:
            for _ in tqdm(range(1, 121)):
                sleep(0.95)

        elif dificuldade == 3:
            for _ in tqdm(range(1, 61)):
                sleep(0.95)

        elif dificuldade == 4:
            for _ in tqdm(range(1, 31)):
                sleep(0.95)

        elif dificuldade == 5:
            for _ in tqdm(range(1, 11)):
                sleep(0.95)

        print()
        print()
        jogo.mostrar_tabuleiro_colorido()

jogo = Palavra('PALAVRA', 16)
jogo.main()


