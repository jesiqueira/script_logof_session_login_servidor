import os


def criar_diretorio(diretorio):
    CSV_DIR = os.path.join(diretorio, "csv")
    FILE_DIR = os.path.join(diretorio, "file")

    if not os.path.isdir(CSV_DIR):
        os.mkdir(CSV_DIR)
    if not os.path.isdir(FILE_DIR):
        os.mkdir(FILE_DIR)



