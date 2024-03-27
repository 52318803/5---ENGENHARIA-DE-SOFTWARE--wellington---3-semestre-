# Crie uma classe chamada Animal com métodos, emitir som e exibir informações básicas sobre o animal (espécie, cor)

class Animal:
    
    def __init__(self, nome, cor_pelo, especie, tamanho, som):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.especie = especie
        self.tamanho = tamanho
        self.som = som
        
    def bicho(self):
        print()
        print(f"Nome do bichano: {self.nome} \n  Especie: {self.especie} \n  Caracteristica: {self.tamanho} \n  Cor: {self.cor_pelo}")
        print(f"Som: {self.som}")
   
   
        
gatinho = Animal("Kitty Pata-Mansa", "Rajada", "Gato", "usa botinha preta e tem uma espada", "MiauMiau")
cachorrinho = Animal("Dog", "Caramelo", "da Rua", "Amigo do Bairro", "AuAuAu")
cobra = Animal("Sogra", "Verde", "Invejosa", "Esticada", "SckSckSck")
tartaruga = Animal("Flash", "Casco marrom c/ perninhas verde", "Veloz", "Maconheira", "Mudo")

gatinho.bicho()
cachorrinho.bicho()
tartaruga.bicho()
cobra.bicho()
