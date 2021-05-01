from util.utilitarios import criar_diretorio
from client.funcionario import Funcionario
import os


f = Funcionario()
f.criar_diretorio(os.getcwd())
opcao = 0
while opcao != 3:
    print("======================== Escolha Opção =====================")
    print('1 - Carregar Base de Dados')
    print('2 - Realizar Logoff')
    print('3 - Sair')
    print('4 - Teste')

    opcao = int(input('Informe sua escolha: '))
    if opcao == 1:
        os.system('cls')
        f.carraga_dados_servidor('jesiqueira')
    elif opcao == 2:
        os.system('cls')
        login = input('Informe o Login para realizar logof: ')
        f.logof(login.strip().lower(), 'jesiqueira')
        os.system('cls')
    elif opcao == 3:
        os.system('cls')
        print('Você saiu')
    else:
        os.system('cls')
        print('Opção selecionada não é Válida')
