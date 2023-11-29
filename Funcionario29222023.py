# Consulta de Funcionario

# Estrutura dic

funcionario = {'Nome':'', 'Salario' : 0.0, 'Ativo': False}

# Apresentação

print('\n\t\t\t -- Consulta de Funcionario -- \n')

# Entrada

funcionario['Nome'] = input('Insira o NOME do funcionario: ')
funcionario['Salario'] = float(input('Insira o SALÁRIO do funcionario em R$: '))
funcionario['Ativo'] = True

# Saída

print(f'Nome: {funcionario["Nome"]}')
print(f'Salário: R${funcionario["Salario"]}')
print("*** Funcionario Ativo ***") if funcionario['Ativo'] else print("*** Funcionario Inativo")

