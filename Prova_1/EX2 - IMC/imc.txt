import pandas as pd
import openpyxl

df = pd.read_excel('dadosmedicossaude.xlsx', engine='openpyxl')  # Aqui foi feita a leitura dos dados
lista = df.values.tolist()

pd.options.display.float_format = '{:.2f}'.format  # Formatando os valores das casas decimais para 2 linhas

df['imc'] = df['peso'] / df['altura'] ** 2  # Cálcula o IMC e gera uma nova coluna com o seu valor para cada paciente

print('       PRÉ VISUALIZAÇÃO DA TABELA')
print(df)

# O critério para os pacientes de maior risco foi definido pelo maior imc dos pacientes que estavam com risco cárdiaco

print('\n\033[35mA tabela nos fornece o imc e o risco, os pacientes com maior risco serão aqueles de maior imc dentro do grupo que possui risco cardiaco\033[m')

print('\n\033[31mPacientes com maior risco de vida: \033[m\n')
for x, y in enumerate(df['imc']):
    if y == max(df['imc']):
        if df['risco cardiaco'][x] == 'Risco':
            print(df['nome do paciente anonimizado'][x], ' IMC: ', df['imc'][x])

print('')

print('O maior imc é: ', end='')   # Faixa de imc
print(max(df['imc']))

print('O menor imc é: ', end='')
print(min(df['imc']))


soma_imc = sum(df['imc'])   # Média dos imc
total = len(df['imc'])
print(f'A média do imc é {soma_imc / total}')

