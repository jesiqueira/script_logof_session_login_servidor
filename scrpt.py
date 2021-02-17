import subprocess

# Lista de Servidores
servidores = [205, 252]

# percorrer todos os servidores da lista e pegar os logins dos colaboradores que estão com session no servidor, após isso salvar dados desse colaboradores no arquivo session.txt
for lista in servidores:
    with open('session.txt', 'a+') as saida:
        list_files = subprocess.run(['query', 'session', f"/server:vbr001vdi-{lista}"], capture_output=True, text=True)
        stdout = f"servidor {lista}\n" + list_files.stdout.strip()        
        # print(list_files.stdout, file=s)
        print(stdout, file=saida)

# Tradar arquivo session.txt e transformar em um arquivo csv para facilitar leitura do arquivo.
with open('session.txt') as list_session:
    with open('pessoas_session.csv', 'w') as saida:
        for texto in list_session:
            if "servidor" in texto:
                servidor = texto[-5::]
            temp =texto[19:-30]
            nome = temp[:10]
            id = temp[-9:]
            if not "SERNAME" in nome and nome.strip(" "):
                print('{}, {}, {}'.format(nome.strip(), id.strip(), servidor.strip()), file=saida)
