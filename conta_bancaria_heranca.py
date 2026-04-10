class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

class ContaPoupanca(Conta_Bancaria):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        self.juros = juros

    def mostrar_saldo(self):
        saldo_total = (f"{self.saldo + (self.saldo * self.juros / 100):,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Titular: {self.titular} | Saldo {saldo_total}€")

class ContaCorrente(Conta_Bancaria):
    def __init__(self, titular, saldo, limite_descoberto ):
        super().__init__(titular, saldo)
        self.limite_descoberto = limite_descoberto

    def mostrar_saldo(self):
        saldo_formatado = (f"{self.saldo:,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        limite_formatado = (f"{self.limite_descoberto:,.2f}").replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Titular {self.titular} | Saldo: {saldo_formatado}€ | Limite: {limite_formatado}€")

conta_poupanca = ContaPoupanca('joão', 1000, 5)
conta_poupanca.mostrar_saldo()
print()
conta_corrente = ContaCorrente('Ana', 2500, 15000)
conta_corrente.mostrar_saldo()