class Transacao:

    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Receita(Transacao):
    pass


class Despesa(Transacao):
    pass


class SistemaFinanceiro:

    def __init__(self):
        self.__transacoes = []

    def adicionar(self, transacao):
        self.__transacoes.append(transacao)

    def mostrar_extrato(self):

        saldo = 0

        print("\n===== EXTRATO =====")

        if len(self.__transacoes) == 0:
            print("Nenhuma transação cadastrada.")
            return

        for t in self.__transacoes:

            if isinstance(t, Receita):
                saldo += t.valor
                print(f"Receita | {t.descricao} | R$ {t.valor:.2f}")

            else:
                saldo -= t.valor
                print(f"Despesa | {t.descricao} | R$ {t.valor:.2f}")

        print(f"\nSaldo atual: R$ {saldo:.2f}")


sistema = SistemaFinanceiro()

while True:

    print("\n===== CONTROLE DE GASTOS =====")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Mostrar extrato")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":

        descricao = input("Descrição: ")

        try:
            valor = float(input("Valor: R$ "))

            receita = Receita(descricao, valor)
            sistema.adicionar(receita)

            print("Receita adicionada com sucesso!")

        except:
            print("Digite um valor válido.")

    elif op == "2":

        descricao = input("Descrição: ")

        try:
            valor = float(input("Valor: R$ "))

            despesa = Despesa(descricao, valor)
            sistema.adicionar(despesa)

            print("Despesa adicionada com sucesso!")

        except:
            print("Digite um valor válido.")

    elif op == "3":

        sistema.mostrar_extrato()

    elif op == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")
