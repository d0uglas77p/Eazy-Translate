### EAZY TRANSLATE pt/en
### Douglas P. Ferreira

import os
from easygoogletranslate import EasyGoogleTranslate
from tkinter import *

#Funcao que limpar o que foi traduzido
def limpar_texto():
    texto_traducao["text"] = ""
    texto_traducao2["text"] = ""
    show_menu()

# Funcao de opcao do menu
def show_menu():
    os.system("cls")
    print("\nEscolha a opção desejada!")
    print("[1] Inglês/Português Br\n[2] Português Br/Inglês\n[3] Observação\n[4] Sair")

# Funcao para traduzir en/pt
def translate_english_to_portuguese():
    translator = EasyGoogleTranslate(source_language='en', target_language='pt', timeout=10)  # Responsável pela traducaoo
    texto_entrada_texto = texto_entrada.get()  # Obtenha o texto da entrada
    result = translator.translate(texto_entrada_texto)

    texto_traducao["text"] = result

# Funcao para traduzir pt/en
def translate_portuguese_to_english():
    translator = EasyGoogleTranslate(source_language='pt', target_language='en', timeout=10)  # Responsável pela traducaoo
    texto_entrada_texto = texto_entrada2.get()  # Obtenha o texto da entrada
    result = translator.translate(texto_entrada_texto)

    texto_traducao2["text"] = result


# Funcao de observacao do programa
def show_observation():
    os.system("cls")
    print("Atenção: EAZY TRANSLATE está em fase de desenvolvimento.\n"
          "Qualquer palavra que for digitado errado ele poderá entender de outra forma!\n"
          "Por favor, digite a palavra correta!\n"
          "No momento contém apenas as traduções em Inglês e Português")


# Função de validação para limitar os caracteres na caixa de entrada
def validate_input_length(P):
    max_length = 99  # definicao máximo desejado
    if len(P) > max_length:
        return False
    return True

### MAIN FRONT
janela = Tk()
janela.title("Eazy Translate")
janela.geometry("750x400")
janela.resizable(False, False)  # Impede a redimensionamento horizontal e vertical


#texto_titulo = Label(janela, text="Eazy")
#texto_titulo.grid(column=7, row=1, padx=200, pady=10)

# Botao para traducao de En/Pt
botao_enpt = Button(janela, text="Traduzir: Inglês / Português", command=translate_english_to_portuguese )
botao_enpt.grid(column=0, row=1, padx=10, pady=20)

# Caixa de entrada do usuario En/Pt
texto_entrada = Entry(janela, width=100, validate="key") #99 caracteres
texto_entrada.grid(column=0, row=2, padx=10, pady=10)

# Texto traduzido da caixa de entrada En/Pt
texto_traducao = Label(janela, width=100, text="")
texto_traducao.grid(column=0, row=3, padx=10, pady=10)

# Botao para traducao de Pt/En
botao_pten = Button(janela, text="Traduzir: Português / Inglês", command=translate_portuguese_to_english )
botao_pten.grid(column=0, row=4, padx=10, pady=20)

# Caixa de entrada do usuario Pt/En
texto_entrada2 = Entry(janela, width=100, validate="key") #99 caracteres
texto_entrada2.grid(column=0, row=5, padx=10, pady=10)

# Texto traduzido da caixa de entrada Pt/En
texto_traducao2 = Label(janela, width=100, text="")
texto_traducao2.grid(column=0, row=6, padx=10, pady=10)

# Botao para limpar
botao_clear = Button(janela, text="Limpar", command=lambda: [limpar_texto(), texto_entrada2.delete(0, 'end'), texto_entrada.delete(0, 'end')])
botao_clear.grid(column=0, row=7, padx=10, pady=10)

# Associacao a função de validação à caixa de entrada/ limites de caracteres da caixa de entrada
validate_input_length_cmd = janela.register(validate_input_length)
texto_entrada.config(validatecommand=(validate_input_length_cmd, '%P'))
texto_entrada2.config(validatecommand=(validate_input_length_cmd, '%P'))

janela.mainloop()