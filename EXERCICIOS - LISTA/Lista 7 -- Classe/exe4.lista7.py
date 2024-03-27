# Crie uma classe chamada Livro com atributos para título, autor e número de páginas. Adicione métodos para exibir informações sobre o livro.

class Biblioteca:
    
    def __init__(self, titulo, autor, num_pag): 
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
        
    def informacoes(self):
        print(f"Nome do Livro: {self.titulo}\n Autor: {self.autor}\n Numero de Pag: {self.num_pag}")
        
    
livro1 = Biblioteca("Historia do Lobo bom", "Nêna", 100)
livro2 = Biblioteca("Nuvens do céu", "nuvem pai", 30)

livro1.informacoes()
print()
livro2.informacoes()        