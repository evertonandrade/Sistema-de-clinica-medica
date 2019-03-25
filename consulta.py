from cadastro import *


# Marcar consulta(medico, paciente, data, hora)
def marcar_consulta():
    dados = {}
    print('Informe seu nome: ')
    #checar se o nome e/ou CPF tem palno
    print('Escolha seu medico')
    # aqui entra a lista de medicos

    dados['data'] = int(input('Qual data?')) # Aqui não importar a data ou hora nesse sistema
    dados['hora'] = int(input('Qual hora?'))

    print('Consulta marcada com sucesso!')
    return dados
