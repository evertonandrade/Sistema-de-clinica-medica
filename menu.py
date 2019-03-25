print('-=-'*20)
print('           SISTEMA DE CLÍNICA MÉDICA     ')
print('-=-'*20)

from cadastro import *

def menu():
    opc = 0
    while opc != 0:
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
        opc = int(input('Qual sua opção? '))
        if opc == 1:
            cadastro_medico()
        if opc == 2:
            cadastro_paciente()



menu()
