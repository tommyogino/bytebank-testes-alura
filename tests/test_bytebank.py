from bytebank import Funcionario
class TestClass:

    def test_idade(self):
        #given-contexto
        entrada = '19/05/2003'
        esperado = 22
        
        #when-ação
        funcionario_teste = Funcionario('Lucas', entrada, 1111)
        resultado = funcionario_teste.idade()

        #then-resultado
        assert resultado == esperado, f'Erro: {resultado} != {esperado}'

    def test_sobrenome(self):
        #given-contexto
        entrada = 'Tommy Ogino'
        esperado = 'Ogino'

        #when-ação
        tommy = Funcionario(entrada, '19/05/2003', 1111)
        resultado = tommy.sobrenome()

        #then-resultado
        assert resultado == esperado, f'Erro: {resultado} != {esperado}'