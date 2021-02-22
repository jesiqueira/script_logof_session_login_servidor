from util.utilitarios import criar_diretorio
from client.funcionario import Funcionario
import os


f = Funcionario()
f.criar_diretorio(os.getcwd())
f.carraga_dados_servidor("lista_servidores.csv", 'jesiqueira')
# if os.path.isfile(os.path.join("csv", "jesiqueira_operador.csv")):
#     os.remove(os.path.join("csv", "jesiqueira_operador.csv"))
