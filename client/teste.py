# from util.utilitarios import criar_diretorio
import os


# print(dir(os))
# print(os.listdir())#lista conteudo do diretório atual
# print(dir(os.path))
# print(os.path.abspath('.'))

# ===== Join =====
# print(os.path.join(os.path.abspath('.'), 'descrição.txt'))

# criar_diretorio(os.getcwd())# os.getcwd -> mostra diretório atual

caminho_arquivo = os.path.join(os.path.abspath('../file')) #Caminho absoluto
arquivo = os.path.join(os.path.abspath('../file'), 'session.txt') #Caminho absoluto
caminho = os.path.join('file', 'session.txt')
print(f"Listar diretório: {os.listdir(caminho_arquivo)}") #listar conteúdo do diretório
print(f"Caminho absoluto: {arquivo}")
print(f"caminho relativo: {caminho}")
print(os.listdir(caminho_arquivo))

# criar_diretorio('downloads')

from util.utilitarios import criar_diretorio
from client.funcionario import Funcionario
import os
from datetime import datetime, timedelta


f = Funcionario()
f.criar_diretorio(os.getcwd())
# f.carraga_dados_servidor("lista_servidores.csv", 'jesiqueira')
# if os.path.isfile(os.path.join("csv", "jesiqueira_operador.csv")):
#     os.remove(os.path.join("csv", "jesiqueira_operador.csv"))
# f.logof()
# data = os.stat(os.path.join('csv', 'jesiqueira_operador.csv')).st_atime
# data_anterior = datetime.fromtimestamp(data)
# data_atual = datetime.now()
# print("Minuto atual: ", data_atual.minute)
# print(data_anterior)
# print(data_atual)
# horas_passadas = data_atual - data_anterior
# print("Horas/minutos passados: ",horas_passadas)
# hms = horas_passadas.seconds / 60
# # print('{:.0f}'.format(hms))
# print("Minutos", int(hms))

# print( int(hms) > 15)


