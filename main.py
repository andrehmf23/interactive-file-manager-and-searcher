from Position import *

#Function Select
while True == True:
    print("Welcome!")
    print("1.Initiate 2.File Hunter 3.Reading directory and run 4.Reading files and run ")
    Z = input("_")
    if Z == '1':
        R = input("Initial name")
        Freceding(R)
        print("FINISH")
        InitialActivate()
        print("FINISH")
        Ferrordetected()
    elif Z == '2':
        R = input("Hunted file")
        Ffilehunter(R)
        print("FINISH")
    elif Z == '3':
        FreadingdirectoryANDrun()
        print("FINISH")
    elif Z == '4':
        FreadingFilesANDrun()
        print("FINISH")
    elif Z == '5':
        print("Errors: ", name_error)
    elif Z == '6':
        Finformation()
    elif Z == '7':
        Fdelete()
    else:
        break

#AUTO
'''
#Diretorio principal
#Achando sala de Encontro(caminho principal)
Freceding("user")
InitialActivate()
#Diretorio dos arquivos
#Achando o caminho da pasta desejada(caminho Secundario)
Ffilehunter("Downloads")
FreadingdirectoryANDrun()
'''


