# Consulta de Funcionario

# Apresentação

print('\n\t\t\t -- Consulta de Funcionario -- \n')

# Entrada

nome = str(input('Insira o NOME do funcionario: '))
salario = float(input('Insira o SALÁRIO do funcionario em R$: '))
ativo = str(input('O funcionario está ATIVO?  S/N  '))

# Processamento e Saída

print(f'Nome: {nome}')
print(f'Salário: R${salario}')

if ativo.lower() =='s':
    print('Ativo')
else:
    print('NÃO ATIVO')

