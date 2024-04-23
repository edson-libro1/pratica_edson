class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"{nome} removido(a) com sucesso!")
                return
        print(f"Funcionário(a) {nome} não encontrado(a).")

    def imprimir_funcionarios(self):
        if self.funcionarios:
            print("Lista de Funcionários:")
            for funcionario in self.funcionarios:
                print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")
        else:
            print("Não há funcionários cadastrados.")

# Testando o programa
empresa = Empresa()

# Adicionando funcionários
empresa.adicionar_funcionario(Funcionario("João", "Desenvolvedor", 5000))
empresa.adicionar_funcionario(Funcionario("Maria", "Gerente de Projetos", 7000))
empresa.adicionar_funcionario(Funcionario("Pedro", "Analista de Dados", 5500))

# Imprimindo a lista de funcionários
empresa.imprimir_funcionarios()

# Removendo um funcionário
empresa.remover_funcionario("Maria")

# Imprimindo a lista atualizada de funcionários
empresa.imprimir_funcionarios()
