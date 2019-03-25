from cadastro import *
from consulta import *
from time import sleep

def menu_interativo():
    while True:
        print('''
        -------------------------------------------
        0. Sair
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
        opc = int(input('Qual sua opção? '))
        if opc == 0:
            print('Saindo...')
            sleep(2)
            break
        if opc == 1:
            cadastro_medico()
        if opc == 2:
            cadastro_paciente()
        if opc == 3:
            marcar_consulta()
        

 
