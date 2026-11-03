
class funcionario:
    def __init__(self, nome, trabalho, **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.trabalho = trabalho

    def trabalhar(self):
        print(f'{self.nome} está trabalhando.')


class precensial(funcionario):
    def __init__(self, bater_ponto, **kwargs):
        super().__init__(**kwargs)
        self.bater_ponto = bater_ponto

    def trabalhar(self):
        print(f'{self.nome}, que trabalha como {self.trabalho}, está trabalhando presencialmente.')


class remoto(funcionario):
    def __init__(self, acessar_sistema, **kwargs):
        super().__init__(**kwargs)
        self.acessar_sistema = acessar_sistema

    def trabalhar(self):
        print(f'{self.nome}, que trabalha como {self.trabalho}, está trabalhando remotamente.')


class hibrido(precensial, remoto):
    def __init__(self, nome, trabalho, bater_ponto, acessar_sistema):
        super().__init__(
            nome=nome,
            trabalho=trabalho,
            bater_ponto=bater_ponto,
            acessar_sistema=acessar_sistema
        )

    def trabalhar(self):
        print(f'{self.nome}, que trabalha como {self.trabalho}, está trabalhando no modelo híbrido.')


# Criando outra classe com herança simples
class desenvolvedor(funcionario):
    def trabalhar(self):
        print(f'{self.nome}, desenvolvedor, está programando.')


# Lista de funcionários
funcionarios = [
    precensial(
        nome='Maria',
        trabalho='Atendente',
        bater_ponto=True
    ),

    remoto(
        nome='Joao',
        trabalho='Desenvolvedor',
        acessar_sistema=True
    ),

    hibrido(
        nome='Pedro',
        trabalho='Analista',
        bater_ponto=True,
        acessar_sistema=True
    ),

    desenvolvedor(
        nome='Carlos',
        trabalho='Programador'
    )
]


# Polimorfismo
for pessoa in funcionarios:
    pessoa.trabalhar()
