print('-=-'*20)
print('           SISTEMA DE CLÍNICA MÉDICA     ')
print('-=-'*20)
print('''
-------------------------------------------
    1. Cadastrar medico
    2. Cadastrar paciente
    3. Marcar consulta
    4.Listar pacientes
    5.Listar Médicos
    6.Listar consulta
    7.Remover médico
    8.Remover consulta
    9.Folha de pagamento médico
    10.Gerar gráficos de consultas
--------------------------------------------
''')
atendimento = int(input('Escolha sua opcao:'))


from cadastro import *

medicos = []
if atendimento == 1:
    while True:
        pergunta1 = input('Cadastrar novo medico[S/N]? ').upper().split()[0]
        if pergunta1 == 'S':
            pass
        else:
            break
        cadastro_medico()
        medicos.append(cadastro_medico)
        print('---'*20)

if atendimento == 2:
    pacientes = []
    while True:
        pergunta2 = input('Cadastrar novo paciente[S/N]? ').upper().split()[0]
        if pergunta2 == 'S':
            pass
        else:
            break
        cadastro_paciente()
        pacientes.append(cadastro_paciente)
        print('---'*20)

if atendimento == 3:
    while True:
        pergunta3 = input('Marcar nova consulta[S/N]? ').upper().split()[0]
        if pergunta3 == 'S':
            pass
        else:
            break
        for k in medicos:
            print(dados['Nome'])



