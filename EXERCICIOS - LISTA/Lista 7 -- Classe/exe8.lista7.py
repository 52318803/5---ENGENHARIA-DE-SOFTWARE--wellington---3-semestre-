# Crie uma classe chamada Estudante com atributos para nome, idade, nota e série. Adicione métodos para atualizar a nota e a série.

class Estudante:
    
    def __init__(self, nome, idade, nota, serie):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.serie = serie
        
    def info(self):
        print(f"Nome: {self.nome} \n idade: {self.idade} \n serie: {self.serie} \n nota: {self.nota}")
        
    def atualizar_nota(self, nova_nota):
        self.nota = nova_nota
        
    def atualizar_serie(self, nova_serie):
        self.serie = nova_serie
        
        
aluno = Estudante("nath", 19, 10, 3)

aluno.info()
print()

aluno.atualizar_nota(8)
aluno.atualizar_serie(4)

print("Aluno atualizado")
aluno.info()
