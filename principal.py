from pacientes import *
from medicos import *
from consulta import *




print(20 * "-=")
print("       SISTEMA DE CLÍNICA MÉDICA")
print(20 * "-=")

print('''--------------------
1 - Pacientes
2 - Médicos
3 - Consultas
4 - Administrativo
--------------------''')

atendimento = int(input("Escolha o tipo de atendimento a ser usado: "))

if atendimento == 1:
    menu_pacientes()
if atendimento == 2:
    menu_medicos()
if atendimento == 3:
    menu_consultas()



