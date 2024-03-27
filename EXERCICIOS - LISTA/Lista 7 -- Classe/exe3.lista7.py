# Crie uma classe chamada Pessoa com atributos para nome, idade e gênero. Adicione métodos para atualizar esses atributos


class pao_queijo:
    
    def __init__(self, goiabada, queijo_branco, requeijao):
        self.goiabada = goiabada
        self.queijo_branco = queijo_branco
        self.requeijao = requeijao
        
    def cafe_tarde(self):
        print(f"Goiabada: {self.goiabada}  Queijo: {self.queijo_branco}  Requeijao: {self.requeijao}")    
        
    def colocar_goiaba(self, add_Goiabada):
        self.goiabada = add_Goiabada
        
    def colocar_queijo(self, add_Queijo):
        self.queijo_branco = add_Queijo
        
    def colocar_requeijao(self, add_Requeijao):
        self.requeijao = add_Requeijao
        
    
paozinho = pao_queijo(0, 0, 0)

paozinho.cafe_tarde()

paozinho.colocar_goiaba(4)
paozinho.colocar_queijo(4)
paozinho.colocar_requeijao(2)

print()
paozinho.cafe_tarde()

