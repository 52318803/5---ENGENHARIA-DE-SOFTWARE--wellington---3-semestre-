# Crie uma classe chamada ContaBancaria que tenha métodos para depositar, sacar e verificar saldo.

class ContaBancaria:
    
    def __init__(self, depositar, sacar, saldo):
        self.depositar = depositar
        self.sacar = sacar
        self.saldo = saldo
        
        
    def colocar(self):
        deposito = self.depositar + self.saldo
        return deposito
    
    def tirar(self):
        saque = self.sacar - self.saldo
        return saque
    
    def saldo(self):
        print(f"Conta Bancaria: {self.saldo}")
        
        
pessoa = ContaBancaria(0, 0, 10)

print("Saldo disponivel: ", pessoa.saldo())

deposito = 50
saque = 15

pessoa.saldo()
