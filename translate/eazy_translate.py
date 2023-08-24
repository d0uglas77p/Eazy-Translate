### EAZY TRANSLATE pt/en
### Douglas P. Ferreira

import os
from time import sleep
from easygoogletranslate import EasyGoogleTranslate

delay=2

#Inicio do programa
print("Bem vindo ao EAZY TRANSLATE...")
sleep(delay)
print("Welcome to EAZY TRANSLATE...")
sleep(delay)

#Menu de Opcoes
os.system("cls")
while True:
    print("\nEscolha a opção desejada!")
    print("[1] Inglês/Português Br\n[2] Português Br/Inglês\n[3] Observação\n[4] Sair")
    opt=input('Opção: ')

    #Se nao informar as opcoes corretas ele ira dar como invalido
    if opt not in ['1', '2', '3', '4']:
        os.system("cls")
        print("\nOpção Inválida")
        input("Precione qualquer tecla para voltar!")
        os.system("cls")

    #Opcao 1: para a traducao de Ingles p Portugues
    os.system("cls")
    if opt=='1':
        translator = EasyGoogleTranslate(source_language='en', target_language='pt', timeout=10) #Responsavel pela traducao

#Loop da opcao 1
        while True:
            print("\n>>>>> Inglês/Português Br <<<<<")
                #Mensgem do usuario
            print("Mensagem: ",end='')
            result = translator.translate(input())
    #Mensagem da traducao
            print("Resultado:", result)
            opt2 = (input("\nPrecione qualquer tecla para continuar!\nDigite V para voltar ao menu! "))
            os.system("cls")

            if opt2 in ['v']: #opcao de voltar ao menu
                opt2 == 'v'
                break #Quebra do loop da opcao 1

    # Opcao 2: para a traducao de Portuguesp Ingles
    elif opt=='2':
        translator = EasyGoogleTranslate(source_language='pt', target_language='en', timeout=10) #Responsavel pela traducao

        while True:
            print("\n>>>>> Português Br/Inglês <<<<<")
            # Mensgem do usuario
            print("Mensagem: ", end='')
            result = translator.translate(input())
            # Mensagem da traducao
            print("Resultado:", result)
            opt2 = (input("\nPrecione qualquer tecla para continuar!\nDigite V para voltar ao menu! "))
            os.system("cls")

            if opt2 in 'v':#opcao de voltar ao menu
                opt2 == 'v'
                break#Quebra do loop da opcao 2

    # Opcao 3: obsercvao do programa exibida p usuario
    elif opt == '3':
        os.system("cls")
        print("Atenção: EAZY TRANSLATE está em fase de desenvolvimento.\n"
              "Qualquer palavra que for digitado errado ele poderá entender de outra forma!\n"
              "Por favor, digite a palavra correta!\n"
              "No momento contém apenas as traduções em Inglês e Português")

##Opcao 4: sair do programa
    elif opt=='4':
        os.system("cls")
        print("Volte sempre ao EAZY TRANSLATE...!")
        sleep(delay)
        break#Quebra do loop principal



