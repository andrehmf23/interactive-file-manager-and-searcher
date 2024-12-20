import os
from shutil import move

name_error = []

director = ""
reset = ""
error = ['Arquivos de Programas', 'Documents and Settings', 'Recovery', 'System Volume Information', '$Recycle.Bin', 'Program Files', 'ProgramData', 'Administrador', 'Aluno', 'Default User', 'Usuário Padrão', 'Windows', 'temp', 'All Users', 'Ambiente de Impressão', 'Ambiente de Rede', 'Configurações Locais', 'Cookies', 'Dados de Aplicativos', 'Menu Iniciar', 'Meus Documentos', 'Modelos', 'Recent', 'SendTo', 'Todos os Usuários', 'Documents', 'AppData']

AutoDelete = True
Mode = 'b'
Del = 'e'
separate = True

Typearquived = []
arquivos = []
caminhos = []
diretorios = []
matrizraiz3 = []
HuntedPath = ""

MeetingDirectory = "NOTHING"
HuntedFolder = "NOTHING"

Identifiedfiletype = [".mp3",".txt"]

# Vetores de Reconhecimento de envio
RecognizedFileType = [".mp3"]
PathNameOfRecognized = ["Extra-Music"]
RecognizedPath = []
RecognizedPathNameCounter = 0

def Finformation():
    print("i___________________________________________________________")
    print("Reading (Finformation)...")
    print("Director: ",director)
    print("MeetingDirectory: ", MeetingDirectory)
    print("Mydir: ",os.getcwd())
    print("HuntedPach: ", HuntedPath)
    print("Reset: ",reset)
    print("Typearquived: ",Typearquived)
    print("Arquivos",arquivos)
    print("Caminhos: ", caminhos)
    print("Diretorios: ", diretorios)
    print("Matrix3: ", matrizraiz3)
    print("____________________________________________________________")

#Encontra a pasta principal
def Freceding(ParamMeetingDirectory):

    global director, MeetingDirectory, reset, HuntedFolder, HuntedPath
    print("r___________________________________________________________")
    print("Reading (Freceding)...")

    MeetingDirectory = ParamMeetingDirectory

    i = 0
    director = ""
    mydir = os.getcwd()

    #Conta quantas casas tem que voltar para encontrar o "MeetingDiretory".
    if mydir.count("\\") != 0:
        #Diminui o diretorio atual do código.
        while i != mydir.count("\\"):
            director = director + "..\\"
            #Se encontrar o diretorio, acaba (Atalho).
            if os.path.exists(director + MeetingDirectory) and MeetingDirectory != "":
                director = director + MeetingDirectory
                break
            i = i + 1
        i = 0
        j = 0
        #Tira a ultima barra (se tiver)
        if director.lower().endswith("\\"):
            for letra in director:
                j = j + 1
            tempt = ""
            for letra in director:
                if i < j - 1:
                    tempt = tempt + letra
                i = i + 1
            director = tempt
        i = 0
        j = 0
        # Tira a ultima barra (se tiver)
        if MeetingDirectory.lower().endswith("\\") or MeetingDirectory.lower().endswith("/"):
            for letra in MeetingDirectory:
                j = j + 1
            tempt = ""
            for letra in MeetingDirectory:
                if i < j - 1:
                    tempt = tempt + letra
                i = i + 1
            MeetingDirectory = tempt

        if director.lower().endswith(".") and MeetingDirectory != "":
            reset = director
            print(director)
            Ffilehunter(MeetingDirectory)
            if HuntedPath != "":
                director = HuntedPath

    print("Director/Reset:", director, "MeetingDirectory:", MeetingDirectory)
    reset = director
    print("r___________________________________________________________")
#Lê o diretorio, apaga os erros(Acesso Negado!) e filtra as pastas no meio dos arquivos

def Fdirectors():

    print("d___________________________________________________________")
    global caminhos, director, diretorios, error, name_error, vetor1, vetor2

    nome = ""
    caminhos = []
    diretorios = []

    try:
        errorn = 0
        z = 0
        while z != len(error):
            if director.count(error[z]) != 0:
                errorn = errorn + 1
                break
            z = z + 1

        if errorn == 0:
            for nome in os.listdir(director):
                if nome != "":
                    caminhos = caminhos + [os.path.join(director, nome)]

            for arq in caminhos:
                if os.path.isdir(arq):
                    if arq != "" and arq != []:
                        diretorios = diretorios + [arq]
            #totaldediretorios = len(diretorios)

    except PermissionError:
        print("Permission error detected!")
        print("Correcting...")
        print(director)
        palavra = ""
        for letra in director:
            if letra != "\\":
                palavra = palavra + letra
            elif letra == "\\" and palavra != "":
                V = False
                i = 0
                while i != len(name_error):
                    if name_error[i] == palavra:
                        V = True
                    i = i + 1
                if V != True:
                    name_error = name_error + [palavra]
                palavra = ""
        name_error = name_error + [palavra]
        i = 0
        x = 0
        while i != len(name_error):
            if i == x:
                if name_error[i] != ".." and name_error[i] != "Users" and name_error[i] != "Andre.exe":
                    error = error + [name_error[i]]
                else:
                    x = x + 1
            i = i + 1
        name_error = []
    print("d___________________________________________________________")

#CAÇADOR DE ARQUIVOS
def Ffilehunter(ParamHuntedFolder):
    global director, diretorios, HuntedFolder, reset, matrizraiz3, HuntedPath

    print("h__________________________________________________________")
    print("Reading (Ffilehunter)...")
    HuntedFolder = ParamHuntedFolder
    print("Folder hunter: ", HuntedFolder)

    i = 0
    j = 0
    k = 0
    setores = 1
    totaldepastas = 1
    matrizraiz = []
    matrizraiz2 = []
    matrizraiz3 = []
    HuntedPath = ""
    anti = 0
    z = 0
    n = 0
    antsetores = 0
    # iv = 0
    jv = 0
    kv = 0
    f = []
    while i == i:
        print(f"i: {i}")
        while j != setores:
            if i != 0:
                if diretorios == []:
                    totaldepastas = f[j]
                Fdirectors()

            while k != totaldepastas:
                if i == 0:
                    Fdirectors()
                    matrizraiz = matrizraiz + [diretorios]
                    n = n + len(diretorios)
                else:
                    if jv != len(f):
                        if kv != f[jv]:
                            #BREAK
                            if director.count(HuntedFolder) != 0:
                                HuntedPath = director

                            director = matrizraiz3[anti][jv][kv]
                            kv = kv + 1
                            if kv == f[jv]:
                                jv = jv + 1
                                kv = 0
                    else:
                        if director.count(HuntedFolder) != 0 and HuntedPath == "":
                            HuntedPath = director
                        z = 1
                        break
                    #ALERT

                    Fdirectors()
                    totaldepastas = len(diretorios)
                    n = n + len(diretorios)
                    if diretorios != []:
                        matrizraiz = matrizraiz + [diretorios]
                k = k + 1
            if matrizraiz != []:
                matrizraiz2 = matrizraiz2 + matrizraiz
            matrizraiz = []
            k = 0
            j = j + 1
            if z == 1:
                break
        if matrizraiz2 != []:
            matrizraiz3 = matrizraiz3 + [matrizraiz2]
        matrizraiz2 = []
        j = 0
        anti = i
        f = []
        g1 = 0
        for t1 in matrizraiz3:
            if g1 == anti:
                for t2 in t1:
                    f = f + [len(t2)]
                    totaldepastas = totaldepastas + len(t2)
            g1 = g1 + 1
        i = i + 1
        antsetores = setores
        setores = n
        n = 0
        jv = 0
        kv = 0
        z = 0
        if HuntedPath != "":
            print("Hunted Path: ",HuntedPath)
            print("Director: ", director, "Reset: ", reset)
            director = reset
            break
        if setores == 0:
            print("Hunted Path not found!")
            print("Director: ", director, "Reset: ", reset)
            director = reset
            break
    print("h__________________________________________________________")

def FreadingdirectoryANDrun():
    print("rd__________________________________________________________")
    print("Reading (FreadingdirectoryANDrun)...")

    global matrizraiz3, HuntedPath, director, arquivos, reset

    director = HuntedPath
    save = HuntedPath
    Ffilehunter("*")


    m = []
    for i in matrizraiz3:
        for j in i:
            for k in j:
                if os.path.isdir(k):
                    m = m + [k]
    i = 0

    print("Matrix read: ", m)

    arquivos = []
    HuntedPath = save
    FreadingFilesANDrun()
    while i != len(m):
        HuntedPath = m[i]
        FreadingFilesANDrun()
        i = i + 1
    print("rd__________________________________________________________")

def FreadingFilesANDrun():
    print("rf__________________________________________________________")
    print("Reading (FreadingFilesANDrun)...")

    global HuntedPath, arquivos, Typearquived, Mode

    caminhos = []
    arquivos = []
    temporary = ""
    Typearquived = []

    # Mexendo no arquivo da pasta desejada
    if os.path.exists(HuntedPath):
        caminhos = [os.path.join(HuntedPath, nome) for nome in os.listdir(HuntedPath)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        print("Arquivos: ", arquivos)

        if Mode == 'b':
            i = 0
            for arq in arquivos:
                for letra in arq:
                    if letra == ".":
                        temporary = ""
                        temporary = temporary + letra
                        i = 1
                    else:
                        temporary = temporary + letra
                        i = i + 1
                if i < 15:
                    Typearquived = Typearquived + [temporary]
                temporary = ""
                i = 0
            print("Typearquived: ", Typearquived)

        print("No files found!!!")
        Fmoving()
    print("rf__________________________________________________________")

def Fmove():
    print("m___________________________________________________________")
    global HuntedPath, arquivos, RecognizedPathNameCounter, RecognizedFileType, RecognizedPath, Typearquived, Mode, Identifiedfiletype
    temporary = ""
    i = 0
    while i != len(arquivos):

        temporary = HuntedPath
        save = HuntedPath
        #temporary = save + Typearquived[i].replace(".","\\")

        if Mode == 'b':
            j = 0
            while j != RecognizedPathNameCounter:
                if Typearquived[i].count(RecognizedFileType[j]) != 0:
                    temporary = RecognizedPath[j]
                j = j + 1
        elif Mode.lower().startswith("a"):

            count = len(Identifiedfiletype)
            HuntedPath = ""

            if reset.count("Desktop") == 0:
                Ffilehunter("Desktop")
                if HuntedPath == "":
                    Freceding("Desktop")
                    HuntedPath = reset
            elif reset.lower().endswith("Desktop"):
                HuntedPath = reset
            else:
                Freturn(reset, "Desktop")

            Research = HuntedPath + "\\" + "Organização"

            if Mode.lower().endswith("o"):
                j = 0
                while j != count:
                    if not os.path.exists(Research + "\\" + Identifiedfiletype[j]):
                        os.mkdir(Research + "\\" + Identifiedfiletype[j])
                        Ffilehunter(Research + "\\" + Identifiedfiletype[j])
                        print("No folder found")
                        print("Folder created in: ", Research)
                        if str(arquivos[i]).lower().endswith(str(Identifiedfiletype[j])):
                            HuntedPath = Research + "\\" + Identifiedfiletype[j]
                    else:
                        if str(arquivos[i]).lower().endswith(str(Identifiedfiletype[j])):
                            HuntedPath = Research + "\\" + Identifiedfiletype[j]
                    j = j + 1

                temporary = HuntedPath
            elif Mode.lower().endswith("u"):
                temporary = Research

        if Mode == 'b':
            if temporary != HuntedPath:
                if os.path.exists(temporary):
                    move(arquivos[i], temporary)
                    print("File moved from ", arquivos[i], " to ", temporary)
                else:
                    os.mkdir(temporary)
            else:
                #print(f"Erro: Mesmo destino! Arquivo: {arquivos[i]}")
                pass
        elif Mode.lower().startswith("a"):
            HuntedPath = save
            if temporary != HuntedPath:
                if os.path.exists(temporary):
                    move(arquivos[i], temporary)
                    print("File moved from ", arquivos[i], " to ", temporary)
                else:
                    os.mkdir(temporary)
            else:
                # print(f"Erro: Mesmo destino! Arquivo: {arquivos[i]}")
                pass
        i = i + 1

    if len(arquivos) == 0 or temporary == HuntedPath:
        print("No files found!!!")
    print("m___________________________________________________________")

def Fmoving():
    print("mg_________________________________________________________")
    print("Reading (Fmoving)...")

    global HuntedPath

    if os.path.exists(HuntedPath):
        Fmove()
    else:
        print("Creating folder...")
        print("Created in: ", HuntedPath)
        os.mkdir(HuntedPath, mode=0o777, dir_fd=None)
        Fmove()
    print("mg_________________________________________________________")

def InitialActivate():
    print("IA_________________________________________________________")
    global RecognizedPath, RecognizedPathNameCounter, PathNameOfRecognized, RecognizedFileType, HuntedPath, reset, Mode

    if Mode == "b":
        # Reconhece se os dois pacotes tem o mesmo tamanho
        if len(RecognizedFileType) == len(PathNameOfRecognized):
            RecognizedPathNameCounter = len(RecognizedFileType)

        # Pré-defini o caminho com base nas especificações
        j = 0
        while j != RecognizedPathNameCounter:
            print("Especial: ",PathNameOfRecognized[j])
            Ffilehunter(PathNameOfRecognized[j])
            print(HuntedPath)

            if HuntedPath == "":
                if reset.count("Desktop") == 0:
                    Ffilehunter("Desktop")
                    if HuntedPath == "":
                        Freceding("Desktop")
                elif reset.lower().endswith("Desktop"):
                    HuntedPath = reset
                else:
                    Freturn(reset,"Desktop")

                if not os.path.exists(HuntedPath + "\\" + PathNameOfRecognized[j]):
                    os.mkdir(HuntedPath + "\\" + PathNameOfRecognized[j])
                    Ffilehunter(HuntedPath + "\\" + PathNameOfRecognized[j])
                    print("No folder found")
                    print("Folder created in: ", HuntedPath)
                else:
                    HuntedPath = HuntedPath + "\\" + PathNameOfRecognized[j]

            RecognizedPath = RecognizedPath + [HuntedPath]
            j = j + 1
        print("RecognizedPath:", RecognizedPath)
    print("IA_________________________________________________________")

def Freturn(Paramreturnpath, Paramhunter):
    print("rn_________________________________________________________")
    global HuntedPath

    Z = ""
    Box = []
    Conter = 0

    for Letra in Paramreturnpath:
        if Letra == '\\':
            Conter = Conter + 1
            Box = Box + [Z]
            Z = ""
        if Letra != '\\':
            Z = Z + Letra

    if Conter + 1 != len(Box):
        Box = Box + [Z]
        Conter = Conter + 1

    Z = ""
    i = 0
    while i != Conter:
        if Box[i] == Paramhunter:
            Z = Z + Box[i]
            break
        else:
            Z = Z + Box[i] + "\\"
        i = i + 1

    HuntedPath = Z
    print("rn_________________________________________________________")
def Fdelete():
    print("d__________________________________________________________")
    print("Reading (Fdelete)...")

    global matrizraiz3, HuntedPath, director, arquivos, reset, Del

    save = director
    Ffilehunter("*")

    HuntedPath = save

    m = [HuntedPath]
    for i in matrizraiz3:
        for j in i:
            for k in j:
                if os.path.isdir(k):
                    m = m + [k]

    print("Matrix read: ", m)

    arquivos = []

    cont = 0
    i = len(m)

    if Del == "e":
        while i != 0:
            nome = os.listdir(m[i-1])
            print(nome)
            if len(nome) == 0:
                print("Pasta: ",m[i-1]," deletada com sucesso!")
                os.rmdir(m[i-1])
            i = i - 1
    elif Del == "a":
        while i != 0:
            nome = os.listdir(m[i-1])
            if len(nome) != 0:
                j = 0
                while j != len(nome):
                    print("Arquivo: ",m[i-1] + "\\" + nome[j], " deletada com sucesso!")
                    os.remove(m[i-1] + "\\" + nome[j])
                    j = j + 1
                print("Pasta: ", m[i - 1], " deletada com sucesso!")
                os.rmdir(m[i - 1])
            else:
                print("Pasta: ", m[i - 1], " deletada com sucesso!")
                os.rmdir(m[i - 1])

            i = i - 1
    print("d__________________________________________________________")
def Ferrordetected():

    global error
    print("--------------Alerta de texto------------")
    if error != []:
        print("Alerta de Erros!")
        print(error)