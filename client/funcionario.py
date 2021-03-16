import os
import csv
import subprocess
from datetime import datetime
import concurrent.futures


class Funcionario:

    def criar_diretorio(self, diretorio):
        CSV_DIR = os.path.join(diretorio, "csv")
        FILE_DIR = os.path.join(diretorio, "file")
        if not os.path.isdir(CSV_DIR):
            os.mkdir(CSV_DIR)
        if not os.path.isdir(FILE_DIR):
            os.mkdir(FILE_DIR)

    def carraga_dados_servidor(self, login_admin):

        namefileServidoresCSV = 'lista_servidores.csv'

        if self._calcTimeCrieteFile(login_admin) > 15:

            self._remover_file(login_admin)

            self._create_file_user_servidor(namefileServidoresCSV, login_admin)

        else:
            print(
                f'Arquivo já existe e foi criado tem menos de { self._calcTimeCrieteFile(login_admin)} minutos')
            opcao = input("Deseja atualizar arquivo agora? Precione 'S/N': ")

            if opcao.lower() == 's':
                os.system('cls')
                print('Carregando Dados.......')
                self._remover_file(login_admin)
                self._create_file_user_servidor(
                    namefileServidoresCSV, login_admin)
                os.system('cls')
                print('Dados Atualizados')

            else:
                print('Opção deseja é não!')

    def _create_file_user_servidor(self, namefileServidoresCSV, login_admin):
        list_server_csv = os.path.join("csv", namefileServidoresCSV)
        file_people = os.path.join("csv", login_admin + "_analista.csv")
        file_session = os.path.join("file", login_admin + "_session.txt")

        with open(list_server_csv) as entrada:
            for servidor in csv.reader(entrada):
                servidores = [int(i) for i in servidor]

        # percorrer todos os servidores da lista e pegar os logins dos colaboradores que estão com session no servidor, após isso salvar dados desse colaboradores no arquivo session.txt
        for lista in servidores:
            with open(file_session, 'a+') as saida:
                list_files = subprocess.run(
                    ['query', 'session', f"/server:vbr001vdi-{lista}"], capture_output=True, text=True)
                stdout = f"servidor {lista}\n" + list_files.stdout.strip()
                print(stdout, file=saida)

        # Tradar arquivo session.txt e transformar em um arquivo csv para facilitar leitura do arquivo.
        with open(file_session) as list_session:
            with open(file_people, 'w') as saida:
                for texto in list_session:
                    if "servidor" in texto:
                        servidor = texto[-5::]
                    temp = texto[19:-30]
                    nome = temp[:10]
                    id = temp[-9:]
                    if not "SERNAME" in nome and nome.strip(" "):
                        print('{}, {}, {}'.format(nome.strip(),
                                                  id.strip(), servidor.strip()), file=saida)

    def _realizarLogof(self, lista):
        _, id, servidor = lista
        logof = subprocess.run(
            ['logoff', f'{int(id)}', f'/server:vbr001vdi-{int(servidor)}'], capture_output=True, text=True)
        return logof

    def _buscarLogin(self, login_operador, login_admin):
        with open(os.path.join('csv', login_admin + '_analista.csv')) as entrada:
            listaPessoa = []
            for pessoa in csv.reader(entrada):
                if pessoa[0] == login_operador:
                    listaPessoa.append(pessoa)

            return listaPessoa

    def logof(self, login_operador, login_admin):
        listAtendente = self._buscarLogin(login_operador, login_admin)
        if len(listAtendente) >= 1:
            print('Realizando Logof, aguarde...')
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.map(self._realizarLogof, listAtendente)

        os.system('cls')
        print('Logof realizado com sucesso!\nExcluindo pasta de usuário do $user')
        self._deletFileUser(login_operador)

    def _remover_file(self, login_admin):
        try:
            os.remove(os.path.join("csv", login_admin + "_analista.csv"))
            os.remove(os.path.join("file", login_admin + "_session.txt"))
        except FileNotFoundError:
            pass

    def _calcTimeCrieteFile(self, login_admin):

        try:
            if os.path.isfile(os.path.join("csv", login_admin + "_analista.csv")):
                data = os.stat(os.path.join(
                    'csv', login_admin + '_analista.csv')).st_atime
                data_anterior = datetime.fromtimestamp(data)
                data_atual = datetime.now()
                tempo_decorrido = data_atual - data_anterior
                minutos = int(tempo_decorrido.seconds / 60)
                return minutos
            else:
                return 1

        except FileNotFoundError as e:
            print('erro ao encontrar arquivo', e)

    def _deletFileUser(self, user_login):
        # if exist "\\vbr001vdi-800\users$\%login%" ( rmdir /s /q "\\vbr001vdi-800\users$\%login%" )
        if os.path.isdir(os.path.join('//vbr001vdi-800/users$/' + user_login)):
            servidor = os.path.join('//vbr001vdi-800/users$/' + user_login)
            try:
                return subprocess.run(['rm', '-rf', f'{servidor}'])
            except ValueError as e:
                print('erro, ', e)
        else:
            print(f'Não foi entrando login: {user_login}')
