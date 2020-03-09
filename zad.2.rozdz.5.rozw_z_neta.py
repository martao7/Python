class gracz():
	def __init__(self):
		self.sila = 0
		self.zrecznosc = 0
		self.zdrowie = 0
		self.modrosc = 0
		self.suma = 30
 
	def powsila(self, liczba):
		if liczba > self.suma:
			print("za mało punktów")
		else:
			self.sila += liczba
			self.suma -= liczba
			print("OK, teraz siła to", self.sila, "zostało ci jeszcze", self.suma, "pónktów do rozdania")
 
	def pomsila(self, liczba):
		if liczba > self.sila:
			print("ma mieć ujemną siłę? Wtedy by umarł pod ciężarem własnego ciała")
		else:
			self.sila -= liczba
			self.suma += liczba
			print("OK, teraz siła to", self.sila, "zostało ci jeszcze", self.suma, "pónktów do rozdania")
 
gracz1 = gracz()
#tutaj zaczynam testy
gracz1.powsila(20)
gracz1.pomsila(15)
gracz1.pomsila(10)
gracz1.powsila(30)
gracz1.powsila(5)
