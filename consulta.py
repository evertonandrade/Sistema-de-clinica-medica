from medicos import *
from pacientes import *


# Marcar consulta(medico, paciente, data, hora)
def marcar_consulta():
    dados = {}
    nome_paciente = input('Informe seu nome: ')
    with open('dados_pacientes.json',) as dados_pacientes:
        lista_pacientes = json.load(dados_pacientes)
        for paciente in lista_pacientes:
            if nome_paciente == paciente['name']:
                print('Vefificado co sucesso ')
                dados['name'] = nome_paciente
            else:
                print('Não encontrado!')
                return marcar_consulta()

    
    with open('dados_medicos.json',) as dados_medicos:
        lista_medicos = json.load(dados_medicos)
        print('Lista de médicos: ')
        for medico in lista_medicos:
            print('* ', medico['name'])
    nome_medico = input('Escolha seu medico:')
    dados['médico'] = nome_medico

    dados['data'] = str(input('Qual data?')) # Aqui não importar a data ou hora nesse sistema
    dados['hora'] = str(input('Qual hora?'))

    print('Consulta marcada com sucesso!')
    return dados


def listar_consultas():
    try:
        with open('dados_consultas.json',) as dados_consultas:
            lista_consultas = json.load(dados_consultas)
            print('Consultas: \n')
            for consulta in lista_consultas:
                print(consulta)
        print('-'*20)
    except:
        print('Nenhuma consulta marcada!')
        

def remover_consulta():
    nome_paciente = input('Informe o nome do paciente: ')
    data_consulta = input('Informe a data da consulta [dd/mm/aaaa]: ')
    try:
        with open('dados_consultas.json') as dados_consultas:
            lista_consultas = json.load(dados_consultas)
            for paciente in lista_consultas:
                if paciente['name'] == nome_paciente and paciente['data'] == data_consulta:
                    lista_consultas.remove(paciente)
                    with open('dados_consultas.json', mode='w') as dados_consultas:
                        consultas = json.dumps(lista_consultas)
                        dados_consultas.write(consultas)
                        print('Consulta removida com sucesso!\n')
                else:
                    print('Consulta não encontrada!\n')
                    menu_consultas()
    except:
        print('Nenhum paciente informado!\n')
        menu_consultas()




def menu_consultas():
    while True:
        print('''1 - Marcar nova consulta
2 - Listar consultas
3 - Sair
        ''')
        opcao = int(input('Selecione uma opção: \n'))
        if opcao == 1:
            try:
                with open('dados_consultas.json') as consultas:
                    antigos_consultas = json.load(consultas)
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    antigos_consultas.append(marcar_consulta())
                    novos_consultas = json.dumps(antigos_consultas)
                    dados_consultas.write(novos_consultas)
            except:
                with open('dados_consultas.json', mode='w') as dados_consultas:
                    novos_consultas = []
                    novos_consultas.append(marcar_consulta())
                    consultas = json.dumps(novos_consultas)
                    dados_consultas.write(consultas)

        elif opcao == 2:
            listar_consultas()
        elif opcao == 3:
            break
        else:
            print("Opção inválida!")
