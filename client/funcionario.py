import os
import csv
import subprocess

class Funcionario:
    
    def criar_diretorio(self, diretorio):
        CSV_DIR = os.path.join(diretorio, "csv")
        FILE_DIR = os.path.join(diretorio, "file")
        if not os.path.isdir(CSV_DIR):
            os.mkdir(CSV_DIR)
        if not os.path.isdir(FILE_DIR):
            os.mkdir(FILE_DIR)
    
    def carraga_dados_servidor(self, namefileServidoresCSV, login):

        list_server_csv = os.path.join("csv", namefileServidoresCSV)
        file_people = os.path.join("csv", login+"_operador.csv")
        file_session = os.path.join("file", login+"_sessio.txt")
        
        if os.path.isfile(file_people):
            os.remove(file_people)
        
        if os.path.isfile(file_session):
            os.remove(file_session)
        
        with open(list_server_csv) as entrada:
            for servidor in csv.reader(entrada):
                servidores = [int(i) for i in servidor]

        # percorrer todos os servidores da lista e pegar os logins dos colaboradores que estão com session no servidor, após isso salvar dados desse colaboradores no arquivo session.txt
        for lista in servidores:
            with open(file_session, 'a+') as saida:
                list_files = subprocess.run(['query', 'session', f"/server:vbr001vdi-{lista}"], capture_output=True, text=True)
                stdout = f"servidor {lista}\n" + list_files.stdout.strip()
                print(stdout, file=saida)

        # Tradar arquivo session.txt e transformar em um arquivo csv para facilitar leitura do arquivo.
        with open(file_session) as list_session:
            with open(file_people, 'w') as saida:
                for texto in list_session:
                    if "servidor" in texto:
                        servidor = texto[-5::]
                    temp =texto[19:-30]
                    nome = temp[:10]
                    id = temp[-9:]
                    if not "SERNAME" in nome and nome.strip(" "):
                        print('{}, {}, {}'.format(nome.strip(), id.strip(), servidor.strip()), file=saida)
    

    def realizarLogof(self, id=0, servidor=0):
        # logoff "%id%" /server:vbr001vdi-"%sv%"
        logof = subprocess.run(['logoff',f'{id}', f'/server:vbr001vdi-{servidor}'], capture_output=True, text=True )
        return logof

    def buscarLogin(self, login_operador, login_admin):
        # with open('pessoas_session.csv') as entrada:
        with open(os.path.join('csv', login_admin + '_operador.csv')) as entrada:
            for pessoa in csv.reader(entrada):
            if pessoa[0] == login_operador:
                return pessoa

    def logof(self, login_operador, login_admin):
        
        listAtendente = self.buscarLogin(login_operador, login_admin)
        _ , id , servidor = listAtendente
        # print(nome)
        returt self.realizarLogof(int(id), int(servidor))
        # realizarLogof(int(id), int(servidor))