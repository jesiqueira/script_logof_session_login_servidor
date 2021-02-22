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


