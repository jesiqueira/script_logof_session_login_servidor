from util.utilitarios import criar_diretorio
from client.funcionario import Funcionario
import os


f = Funcionario()
f.criar_diretorio(os.getcwd())
# f.carraga_dados_servidor("lista_servidores.csv", 'jesiqueira')
# f.logof()
# data = os.stat(os.path.join('csv', 'jesiqueira_operador.csv')).st_atime
# data_anterior = datetime.fromtimestamp(data)
# data_atual = datetime.now()
# horas_passadas = data_atual - data_anterior
# hms = horas_passadas.seconds / 60
opcao = 0
while opcao != 3:
    print("======================== Escolha Opção =====================")
    print('1 - Carregar Base de Dados')
    print('2 - Realizar Logoff')
    print('3 - Realizar Sair')

    opcao = int(input('Informe sua escolha: '))
    if opcao == 1:
        os.system('cls')
        f.carraga_dados_servidor("lista_servidores.csv", 'jesiqueira')
    elif opcao == 2:
        os.system('cls')
        login = input('Informe o Login para realizar logof: ')
        f.logof(login, 'jesiqueira')
        os.system('cls')
    elif opcao == 3:
        os.system('cls')
        print('Você saiu')
    else:
        os.system('cls')
        print('Opção selecionada não é Válida')
