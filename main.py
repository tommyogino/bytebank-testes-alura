from bytebank import Funcionario

#tommy = Funcionario('Tommy Ogino', '19/05/2003', 2000)

#print(tommy.idade())

def teste_idade():
    Funcionario_teste = Funcionario('teste' , '19/05/2003', 2000)
    print(f'teste = {Funcionario_teste.idade()}')

    Funcionario_teste1 = Funcionario('teste' , '19/05/2000', 2000)
    print(f'teste = {Funcionario_teste1.idade()}')

    Funcionario_teste2 = Funcionario('teste' , '19/05/1967', 2000)
    print(f'teste = {Funcionario_teste2.idade()}')



teste_idade()