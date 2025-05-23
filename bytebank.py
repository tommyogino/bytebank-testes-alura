from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    
    def _eh_socio(self):
        sobrenomes = ['Braganca', 'Windsor', 'Bourbon', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000 and self.sobrenome() in sobrenomes)
        # Método privado para verificar se o funcionário é sócio
        # de acordo com o sobrenome e o salário 

    def decresimo_salario(self):
            if self._eh_socio():
                decresimo = self.salario * 0.1
                self._salario = self._salario - decresimo
        
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('Salario muito alto para receber bonus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'