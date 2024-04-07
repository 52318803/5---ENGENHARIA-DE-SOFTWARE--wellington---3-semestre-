# Desenvolva uma agenda de contatos onde diferentes tipos de contatos 
# (por exemplo, pessoal, profissional, médico) tenham diferentes métodos para armazenar 
# informações adicionais (como endereço, número de telefone, especialidade).


class contatos:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pessoal(contatos):
    def nom(self):
        return self.nome

    def numero(self):
        return self.telefone
    
    def ender(self):
        return self.endereco
    

class Profissional(contatos):
    def nom(self):
        return self.nome

    def numero(self):
        return self.telefone
    
    def ender(self):
        return self.endereco
    
    
class Medico(contatos):
    def nom(self):
        return self.nome

    def numero(self):
        return self.telefone
    
    def ender(self):
        return self.endereco
    
    
    
pessoa = [Pessoal("Creuza", 123654789, "asdfghjkiuy"), 
          Profissional("Jose", 753215964, "gbfdifujiuf"), 
          Medico("Paulo", 48848685, "iweroikvsd")]


for info in pessoa:
    print(info.nom())
    print(info.numero())
    print(info.ender())
    print()