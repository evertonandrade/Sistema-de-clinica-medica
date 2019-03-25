#Cadastro de paciente
def cadastro_paciente():
    dados = {}
    dados['name'] = input('Nome: ')
    dados['email'] = input('Email:')
    dados['phone'] = input('Telefone: ')
    dados['rg'] = input('RG: ')
    dados['cpf'] = input('CPF: ')
    dados['number'] = input('Endereço: ')
    dados['address'] = input('número: ')
    dados['hood']= input('Bairro: ') 
    dados['city']= input('Cidade: ')
    dados['estado'] = input('UF: ')
    dados['plano'] = input('Plano de saúde: ')
    print('Cadastrado com sucesso!')
    return dados


#Cadastro de médico
def cadastro_medico():
    dados = {}
    dados['name'] = input('Nome: ')
    dados['email'] = input('Email:')
    dados['phone'] = input('Telefone: ')
    dados['cell'] = input('Celular: ')
    dados['crm'] = input('CRM: ')
    dados['rg'] = input('RG: ')
    dados['cpf'] = input('CPF: ')
    dados['number'] = input('Endereço: ')
    dados['specialization'] = input('Especialização: ')
    dados['address'] = input('número: ')
    dados['hood']= input('Bairro: ') 
    dados['city']= input('Cidade: ')
    dados['estado'] = input('UF: ')
    dados['plano'] = input('Plano de saúde: ')



