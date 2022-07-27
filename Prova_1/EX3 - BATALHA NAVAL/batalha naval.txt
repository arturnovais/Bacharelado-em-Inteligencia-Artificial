def definindo_posicao(f='\033[97mDigite a posição de início do barco: \033[m'):
    valores = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j']  # Essa lista contem o valor númerico referente as letras, a partir do índice da lista, para eu poder substituir no valor da coluna
    while True:  # Verificação da posição
        inteiro = letra = 0

        print('\n\033[30mInsira a posição desse modo: 1A, 3C...\033[m')
        posicao = str(input(f'{f}'))

        if len(posicao) == 2:  # Verificando se o usuário inseriu uma posição com linha e coluna
            for i in posicao:
                if i.isnumeric():
                    inteiro += 1
                elif not i.isnumeric():
                    letra += 1
            if letra == 1 and inteiro == 1:  # Verificando se o usuário inseriu um valor para linha e outro para coluna
                break

    for char in posicao.lower():  # Definindo o valor da linha e coluna
        if char.isnumeric():
            linha = int(char)
        elif not char.isnumeric():
            coluna = valores.index(char)

    return linha, coluna


def definindo_direcao():
    while True:  # Verificação da direção
        erro = False
        try:
            print('\n\033[30mHorizontal = [H] / Vertical = [V]\033[m')
            direcao = input('Digite a direção: ')[0].strip()
            if direcao in 'HhVv':
                break

        except ValueError:
            print(
                'Você deve digitar um valor')  # Essa função só retorna um valor quando o usuário digitar ele corretamente
            erro = True

        if not erro:
            print('Você deve digitar H para horizontal e V para vertical')

    return direcao.upper()


class BatalhaNaval:
    def __init__(self, dificuldade=1):
        self.dificuldade = dificuldade  # A dificuldade possui 2 níveis, o nível 1 (Fácil) e o nível 2 (Difícil)

        self.campo1 = []  # Campo 1 e onde estão os seus barcos, não os irei adicionar direto ao campo 1 para não ficarem vísiveis no print
        self.posicao_barcos1 = []
        self.ataques1 = []
        self.vidas1 = 11

        self.campo2 = []    # Campo 2 e onde estão os seus barcos, não os irei adicionar direto ao campo 1 para não ficarem vísiveis no print
        self.posicao_barcos2 = []
        self.ataques2 = []
        self.vidas2 = 11

        self.tabuleiro = []  # O tabuleiro é um tensor que recebe o campo 1 e o campo 2

        # Definindo o tamanho dos navios
        self.rebocador = 2
        self.contratorpedeiro = 2
        self.cruzador = 3
        self.portaavioes = 4

        self.navios = [self.rebocador, self.contratorpedeiro, self.cruzador,
                       self.portaavioes]  # Lista com o tamanho dos navios
        self.nomes_navio = ['Rebocador', 'Contratorpedeiro', 'Cruzador', 'Portaavioes']  # Lista com o nome dos navios

    def pegar_tamanho(self):
        if self.dificuldade == 1:
            return 6
        else:
            return 10

    def gerando_o_campo(self):  # Essa função inicializa a matriz do campo 1 e 2 e depois adiciona elas ao tabuleiro
        linha = []

        if self.dificuldade == 1:  # A dificuldade 1 gera um campo 6x6, e a 2 um campo 10x10
            campo = 6
        elif self.dificuldade == 2:
            campo = 10

        for i in range(
                campo):  # Esse laço adiciona ao vetor campo outros vetores, onde cada um é uma linha, e assim transformando o campo em uma matriz
            for j in range(campo):
                linha.append('.')  # Inicializa os campos com as posições preenchidas por 'x'
            self.campo1.append(linha[:])
            self.campo2.append(linha[:])
            linha.clear()

        self.tabuleiro.append(self.campo1)
        self.tabuleiro.append(self.campo2)

    def mostrar_tabuleiro(self):  # Essa função mostra o tabuleiro contendo o campo 1 e 2

        for c, campos in enumerate(self.tabuleiro):

            if self.dificuldade == 1:  # Imprime as letras conforme o tamanho da matriz, influenciada pela dificuldade
                print(f'\033[97m\033[40m       CAMPO {c + 1}       \033[m')
                print('    A  B  C  D  E  F')

            if self.dificuldade == 2:
                print(f'\033[97m\033[40m             CAMPO {c + 1}             \033[m')
                print('    A  B  C  D  E  F  G  H  I  J')

            for cont, campo in enumerate(campos):
                print(f'{cont:2}', end='  ')
                for posicao in campo:
                    print(f'\033[34m{posicao}\033[m', end='  ')
                print()
            print()

    def mostrar_tabuleiro_colorido(self):

        for c, campos in enumerate(self.tabuleiro):

            if self.dificuldade == 1:  # Imprime as letras conforme o tamanho da matriz, influenciada pela dificuldade
                print(f'\033[97m\033[40m       CAMPO {c + 1}       \033[m')
                print('    A  B  C  D  E  F')

            if self.dificuldade == 2:
                print(f'\033[97m\033[40m             CAMPO {c + 1}             \033[m')
                print('    A  B  C  D  E  F  G  H  I  J')

            for cont, campo in enumerate(campos):
                print(f'{cont:2}', end='  ')
                for posicao in campo:
                    if posicao == 'O':
                        print(f'\033[32m{posicao}\033[m', end='  ')
                    elif posicao == 'X':
                        print(f'\033[31m{posicao}\033[m', end='  ')
                    else:
                        print(f'\033[34m{posicao}\033[m', end='  ')
                print()
            print()


    def percorrendo_matriz(self, matriz, navio, direcao, l, c):         # Essa função foi criada para impedir a sobreposição

        for i in range(navio):
            for linha in matriz:                            # Ele vai percorrer todas as posições onde vamos inserir o barco
                if linha[0] == l and linha[1] == c:         # Caso ele não passe por uma posição ocupada ele vai retornar que o barco pode ser inserido nessa posição
                    return 'erro'
            if direcao == 'V':
                l += 1
            else:
                c += 1

        return 'livre'

    def inserindo_os_navios(self, jogador):  # Essa função adiciona os navios no tabuleiro
        from time import sleep
        campo = []  # Lista onde vou inserir varías lista com as posições onde os barcos estão
        posicao = []
        tamanho_campo = self.pegar_tamanho()

        print(f'\n\033[44m            \033[1;97mJOGADOR {jogador}              \033[m')

        for cont, navio in enumerate(self.navios):  # Percorre os navios existentes, para adicionar posição a cada um deles
            sleep(0.55)
            print(f'\n\033[1;97m{cont + 1} ---> \033[m /\033[30m\033[47mVamos adicionar o navio \033[1;30m{self.nomes_navio[cont]}\033[m\033[30m\033[47m ele ocupa \033[31m{navio}\033[47m\033[30m espaços\033[m/')

            while True:    # Loop gerado para que só seja quebrado quando o usuário digitar uma posição válida, isto é: sem contrapoisão e que esteja dentro da matriz campo
                linha, coluna = definindo_posicao()
                direcao = definindo_direcao()

                if direcao == 'H':  # Insere a posição de acordo com a direção horizontal

                    if coluna > tamanho_campo - navio:          # Verifica se o usuário não vai inserir o navio numa posição que vai parar fora da matriz
                        print('Não é possível adicionar o navio nessa posição')

                    else:
                        inserir = self.percorrendo_matriz(campo, navio, direcao, linha, coluna)  # Percorre as posições onde o barco vai ficar, onde ele só o vai inserir nela caso estejam todas livres, evitando assim a sobreposição

                        if inserir == 'erro':
                            print('\033[31mJá existe um barco nessa posição\033[m')

                        else:
                            for co in range(navio):
                                posicao.append(linha)
                                posicao.append(coluna)
                                campo.append(posicao[:])
                                posicao.clear()
                                coluna += 1

                            print(f'\033[32m\nNavio {self.nomes_navio[cont]} adicionado ao campo\033[m\n')
                            sleep(0.55)
                            break


                if direcao == 'V':          # Insere a posição de acordo com a direção vertical

                    if linha > tamanho_campo - navio:       # Verifica se o usuário não vai inserir o navio numa posição que vai parar fora da matriz
                        print('\033[31mNão é possível adicionar o navio nessa posição\033[m')

                    else:
                        inserir = self.percorrendo_matriz(campo, navio, direcao, linha, coluna)  # Percorre as posições onde o barco vai ficar, onde ele só o vai inserir nela caso estejam todas livres, evitando assim a sobreposição

                        if inserir == 'erro':
                            print('\033[31mJá existe um barco nessa posição\033[m')    # Caso exista um barco nessa posição ele vai retornar essa mensagem, e ele não executa a condição necessaria para adicionar a posição na matriz
                        else:                                                          # Assim pedindo uma nova posição ao usuário
                            for con in range(navio):
                                posicao.append(linha)
                                posicao.append(coluna)                                 # Com a condição necessária ele vai gerar uma lista de posições com [linha, coluna] e inserir essa lista na lista campo
                                campo.append(posicao[:])
                                posicao.clear()
                                linha += 1

                            print(f'\033[32m\nNavio {self.nomes_navio[cont]} adicionado ao campo\033[m\n')
                            sleep(0.55)
                            break


        if jogador == 1:
            self.posicao_barcos1 = campo[:]       # Ele adiciona a lista campos numa lista que salva as posições dos barcos em cada campo
        else:                                     # Essa lista foi criada para não mostrar as posições em que inseri o barco e acabar com a graça do jogo
            self.posicao_barcos2 = campo[:]

        return

    def ataque(self, jogador):      # Nessa função o usuário escolhe uma posição Aij e realiza um ataque
        from time import sleep

        ataque = []

        if jogador == 1:
            campo = self.posicao_barcos2    # Defini o campo de acordo com o jogador
            ataques = self.ataques1
        elif jogador == 2:
            campo = self.posicao_barcos1
            ataques = self.ataques2

        print('\n\033[1;97m\033[41mHORA DE ATACAR\n\033[m')
        sleep(1)
        self.mostrar_tabuleiro()
        print(f'\n\033[44m            \033[1;97mJOGADOR {jogador}              \033[m')

        while True:
            linha_atk, coluna_atk = definindo_posicao('\033[97mDigite a posição onde deseja lançar um míssil: \033[m')  # Defini a linha e coluna que o usuário vai atacar

            ataque.append(linha_atk)
            ataque.append(coluna_atk)

            if ataque not in ataques:  # Verifica se o ataque já não foi executado, e só sai do loop caso ainda nçao tenha sido
                break

            else:
                print('\033[1;31mEste ataque já foi realizado, por favor insira outras cordenadas\033[m')
                ataque.clear()

        for pos in campo:          # Percorre o campo do jogador adversário
            if linha_atk == pos[0] and coluna_atk == pos[1]:  # Faz a verificação se a linha esolhida tem um barco
                acertou = True
                break
            else:
                acertou = False

        if acertou:     # Caso a linha escolhida tenha um barco ele vai decrementar uma vida do usuário, que possui como quantidade de vidas o tamanho de seus barcos
            if jogador == 1:
                self.vidas2 -= 1
            else:
                self.vidas1 -= 1

            print('\033[1;32m\nVocê acertou um alvo\033[m')
            if jogador == 1:
                self.campo2[linha_atk][coluna_atk] = 'O'   # Ele substitui o '.' no mar pelo O, que significa 'Posição com barco'
            elif jogador == 2:
                self.campo1[linha_atk][coluna_atk] = 'O'

        else:
            if jogador == 1:
                self.campo2[linha_atk][coluna_atk] = 'X'   # Ele substitui o '.' no mar pelo X, que significa 'Posição sem barco'
            elif jogador == 2:
                self.campo1[linha_atk][coluna_atk] = 'X'
            print('\033[1;31m\nVocê não acertou o alvo\033[m')

        if jogador == 1:
            self.ataques1.append(ataque[:])         # Cria a lista de ataques, para fazer a verificação quando for inserir um novo ataque

        elif jogador == 2:
            self.ataques2.append(ataque[:])

        ataque.clear()

        return

    def main(self):   # Função que defini a ordem de chamada dos métodos da classe
        print('\033[41m\033[30m   DIFICULDADE   \033[m')
        print('1 - Gera uma matriz 6x6 '
              '\n2 - Gera uma matriz 10x10')
        while True:
            try:
                erro = False
                dificuldade = int(input('\n\033[97mDigite a dificuldade do jogo:\033[m '))
                if 0 < dificuldade <= 2:
                    break
            except ValueError:
                erro = True
                print('Digite 1 para fácil, 2 para difícil')

            if not erro:
                print('Digite 1 para fácil, 2 para difícil')

        self.dificuldade = dificuldade

        from time import sleep
        print()
        print()
        self.gerando_o_campo()
        self.mostrar_tabuleiro()
        self.inserindo_os_navios(1)
        print('\n' * 20)
        self.mostrar_tabuleiro()
        self.inserindo_os_navios(2)

        while True:
            self.mostrar_tabuleiro_colorido()
            sleep(2)
            self.ataque(1)
            if self.vidas2 == 0:
                print('\033[32mO JOGADOR 1 GANHOU!!!\033[m')
                break
            self.mostrar_tabuleiro_colorido()
            sleep(2)
            self.ataque(2)
            if self.vidas1 == 0:
                print('\033[32mO JOGADOR 2 GANHOU!!!\033[m')
                break




jogo = BatalhaNaval(1)
jogo.main()
