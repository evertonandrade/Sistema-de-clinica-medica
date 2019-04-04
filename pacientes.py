import json

def cadastro_paciente():
        dados = {}
        dados['name'] = input('Nome: ')
        dados['email'] = input('Email:')
        dados['phone'] = input('Telefone: ')
        dados['rg'] = input('RG: ')
        dados['cpf'] = input('CPF: ')
        dados['number'] = input('Endereço: ')
        dados['address'] = input('número: ')
        dados['hood'] = input('Bairro: ')
        dados['city'] = input('Cidade: ')
        dados['estado'] = input('UF: ')
        dados['plano'] = input('Plano de saúde: ')
        print('Cadastrado com sucesso! \n\n')
        return dados


def listar_pacientes():
    try:
        with open('dados_pacientes.json',) as dp:
            arq_pacientes = json.load(dp)
            print('Pacientes: \n')
            for paciente in arq_pacientes:
                print(paciente['name'])
        print('-'*20)
    except:
        print('Nenhum paciente cadastrado!')


def remover_paciente():
    try:
        with open('dados_pacientes.json') as dados_pacientes:
            lista_pacientes = json.load(dados_pacientes)
            cpf = input('Qual o CPF do paciente que você deseja remover?')
            for paciente in lista_pacientes:
                if paciente['cpf'] == cpf:
                    lista_pacientes.remove(paciente)
                    with open('dados_pacientes.json', mode='w') as dados_pacientes:
                        pacientes = json.dumps(lista_pacientes)
                        dados_pacientes.write(pacientes)
                    print('Paciente removido com sucesso!\n')
                else:
                    print('Paciente não encontrado!\n')
                    menu_pacientes()
    except:
        print('Nenhum CPF informado')
        menu_pacientes()


def menu_pacientes():
    while True:
        print('''1 - Cadastrar novo paciente
2 - Listar pacientes
3 - Remover paciente
4 - Sair
        ''')
        opcao = int(input('Selecione uma opção: \n'))
        if opcao == 1:
            try:
                with open('dados_pacientes.json') as pacientes:
                    antigos_pacientes = json.load(pacientes)
                with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    antigos_pacientes.append(cadastro_paciente())
                    novos_pacientes = json.dumps(antigos_pacientes)
                    dados_pacientes.write(novos_pacientes)
            except:
                with open('dados_pacientes.json', mode='w') as dados_pacientes:
                    novos_pacientes = []
                    novos_pacientes.append(cadastro_paciente())
                    pacientes = json.dumps(novos_pacientes)
                    dados_pacientes.write(pacientes)

        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            remover_paciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")