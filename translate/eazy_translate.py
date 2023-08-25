### EAZY TRANSLATE pt/en
### Douglas P. Ferreira

import os
from time import sleep
from easygoogletranslate import EasyGoogleTranslate

#Funcao de inicio
def welcome_message():
    print("Bem vindo ao EAZY TRANSLATE...")
    sleep(delay)
    print("Welcome to EAZY TRANSLATE...")
    sleep(delay)

#Funcao de opcao do menu
def show_menu():
    os.system("cls")
    print("\nEscolha a opção desejada!")
    print("[1] Inglês/Português Br\n[2] Português Br/Inglês\n[3] Observação\n[4] Sair")

#Funcao para traduzir en/pt
def translate_english_to_portuguese():
    translator = EasyGoogleTranslate(source_language='en', target_language='pt', timeout=10) #Responsavel pela traducao
    while True:
        print("\n>>>>> Inglês/Português Br <<<<<")
        print("Mensagem: ", end='')
        result = translator.translate(input())
        print("Resultado:", result)
        opt2 = input("\nPrecione qualquer tecla para continuar!\nDigite V para voltar ao menu! ")
        os.system("cls")
        if opt2.lower() == 'v':
            break
#Funcao para traduzir pt/en
def translate_portuguese_to_english():
    translator = EasyGoogleTranslate(source_language='pt', target_language='en', timeout=10)#Responsavel pela traducao
    while True:
        print("\n>>>>> Português Br/Inglês <<<<<")
        print("Mensagem: ", end='')
        result = translator.translate(input())
        print("Resultado:", result)
        opt2 = input("\nPrecione qualquer tecla para continuar!\nDigite V para voltar ao menu! ")
        os.system("cls")
        if opt2.lower() == 'v':
            break

#Funcao de observacao do programa
def show_observation():
    os.system("cls")
    print("Atenção: EAZY TRANSLATE está em fase de desenvolvimento.\n"
          "Qualquer palavra que for digitado errado ele poderá entender de outra forma!\n"
          "Por favor, digite a palavra correta!\n"
          "No momento contém apenas as traduções em Inglês e Português")

delay = 2
# Inicio do programa
welcome_message()

while True:
    show_menu()
    opt = input('Opção: ')

    if opt not in ['1', '2', '3', '4']:
        os.system("cls")
        print("\nOpção Inválida")
        input("Precione qualquer tecla para voltar!")
        os.system("cls")

    #Escolha de opcoes
    elif opt == '1':
        translate_english_to_portuguese()
    elif opt == '2':
        translate_portuguese_to_english()
    elif opt == '3':
        show_observation()
    elif opt == '4':
        os.system("cls")
        print("Volte sempre ao EAZY TRANSLATE...!")
        break  # Quebra do loop principal


