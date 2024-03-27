# Crie uma classe chamada Calendario que tenha métodos para receber a data atual, verificar se é um ano bissexto e exibir o dia da semana

'''
import datetime

class Calendario:
    def _init_(self):
        self.data_atual = datetime.date.today()

    def verificar_ano_bissexto(self, ano):
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            return True
        else:
            return False

    def exibir_dia_da_semana(self):
        dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        indice_dia_semana = self.data_atual.weekday()
        return dias_da_semana[indice_dia_semana]

    def exibir_informacoes(self):
        print("Data atual:", self.data_atual.strftime("%d/%m/%Y"))
        if self.verificar_ano_bissexto(self.data_atual.year):
            print("O ano atual é bissexto.")
        else:
            print("O ano atual não é bissexto.")
        print("Dia da semana:", self.exibir_dia_da_semana())

calendario = Calendario()
calendario.exibir_informacoes()

'''

from datetime import date

class Calendario:
    def _init_(self):
        self.data_atual = date.today()

    def ano_bissexto(self, ano):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return "é ano bissexto"
        else:
            return "não é ano bissexto"

    def dia_da_semana(self):
        dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        return dias_da_semana[self.data_atual.weekday()]

#Imprimir informações
    
calendario = Calendario()

print("Data atual:", calendario.data_atual)
print("Ano bissexto:", calendario.ano_bissexto(calendario.data_atual.year))
print("Dia da semana:", calendario.dia_da_semana())