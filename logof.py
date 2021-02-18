import subprocess
import csv


def realizarLogof(id=0, servidor=0):
    # logoff "%id%" /server:vbr001vdi-"%sv%"
    logof = subprocess.run(
        ['logoff', f'{id}', f'/server:vbr001vdi-{servidor}'], capture_output=True, text=True)
    print(logof)


def buscarLogin(login):
    with open('pessoas_session.csv') as entrada:
        for pessoa in csv.reader(entrada):
            if pessoa[0] == login:
                return pessoa


listAtendente = buscarLogin('jesiqueira')
nome, id, servidor = listAtendente
print(nome)
realizarLogof(int(id), int(servidor))
