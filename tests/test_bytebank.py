from bytebank import Funcionario
import pytest
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

    def test_decresimo_salario(self):

        #given-contexto
        entrada = 100000
        entrada_nome = 'Paulo Braganca'
        esperado = 90000

        #when-acao
        funcionario_teste = Funcionario(entrada_nome, '19/05/2003', entrada)
        funcionario_teste.decresimo_salario()
        resultado = funcionario_teste.salario

        #then-resultado
        assert resultado == esperado, f'Erro: {resultado} != {esperado}'

    def test_calcular_bonus(self):
        
        #given-contexto
        entrada = 1000
        esperado = 100

        #when-acao
        funcionario_teste = Funcionario('Lucas', '19/05/2003', entrada)
        resultado = funcionario_teste.calcular_bonus()

        #then-resultado
        assert resultado == esperado, f'Erro: {resultado} != {esperado}'

    def test_calcular_bonus_exception(self):

        #given-contexto
        with pytest.raises(Exception):
            entrada = 1000000000

            #when-acao
            funcionario_teste = Funcionario('Lucas', '19/05/2003', entrada)
            resultado = funcionario_teste.calcular_bonus()

            #then-resultado
            assert resultado

    