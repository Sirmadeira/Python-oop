#Um metodo regular automaticamente pega a instancia como o primeiro argumento, ou seja, tem self.
#Um metodo de classe. E mais utilizado para definir a classe em si, do que para a instancia.Ele se utiliza do argumento cls,
#Ele tambem e utilizar para construtures alternativos
#Um metodo statico, nao recebe argumentos nem da classe, nem das instancias. Ele geralmente, e utilizado. Quando voce tem uma funcao
#Que e associada a sua classe mas n precisa de outros argumentos.

class Trabalhador:
#Variaveis de classe, sao compartilhadas por todas as instancias
	num_of_trabs=0
	aumento_salario=1.04
	#Exemplo de metodo regular
	def __init__(self,nome,sobrenome,salario):# Self e convencao
		self.nome=nome
		#Isso daki e um atributo 
		self.sobrenome= sobrenome
		self.salario = salario
		self.email= nome+'.'+sobrenome+'@gmail.com'

		Trabalhador.num_of_trabs+=1
		#Nesse caso por exemplo, eu n preciso altera isso logo ja do call diretamente em Trabalhador, porque todas as instancias nao variam nesse quesito.
	#pass #- Quebra a classe
	# Instancias sao partes de uma classe, cada trabalhador criado e uma instancia. O que cria e a classe.
	def nomecompleto(self):
		return f'Nome completo {self.nome} {self.sobrenome}'
	def acrescentar_salario(self):
		self.salario =int(self.salario * self.aumento_salario)
		#Self.aumento_salario e melhor do que Trabalhador.aumento_salaro porque caso eu queira mudar uma instancia de alguem especifico como trab1 eu consigo
	#Isso daki e um metodo de classe
	@classmethod
	def definir_aumento_salario(cls,quantidade):
		cls.aumento_salario = quantidade
	@classmethod
	def de_string(cls,trab_str):
		#Funcao de classe exemplo, ela vai rachar a string pelo o user
		#Ao inves, de ter que trabalhar pela instancia da string especifica, ele pode trabalhar por qualquer string
		#Devido ao class method
		nome,sobrenome,salario = trab_str.split('-')
		return cls(nome,sobrenome,salario)
		#Para ele ser capaz de receber o objeto do trabalhado
	#Isso daki e um metodo statico
	@staticmethod
	def dia_trabalho(dia):
		if dia.weekday()==5 or dia.weekday()==6:
			return False
		return True
	#Como voce pode ver eu n ao recebi nenhum metodo ou variavel externa.	


trab_1=Trabalhador('Jose','Antonio',50000)#Exemplo de instancia
trab_2=Trabalhador('Antonio','Batata',6000)


print(trab_1.email)

print(trab_2.email)#Atributos nao precisam de parantese

print(trab_1.salario)
#trab_1.acrescentar_salario()
Trabalhador.definir_aumento_salario(1.05)
#Utilizando do class method
print(trab_1.salario)
print(trab_1.aumento_salario)
print(trab_1.nomecompleto()) #Metodos precisam de parenteses)
#No caso acima nao
print(Trabalhador.nomecompleto(trab_1))
#Nesse caso precisa passar a instancia pq nao identifica qm seria o self
print(trab_1.__dict__)
#Dict faz um dicionario com todos os atributos definido
print(Trabalhador.num_of_trabs)
	
trab_novo_str_1='Joao-Antonio-6000'
#Exemplo de metodo de classe a ser convertido
novo_trab=Trabalhador.de_string(trab_novo_str_1)
#Conversao do metodo de classe
print(novo_trab.email)

import datetime
minha_data = datetime.date(2016,6,10)
print(Trabalhador.dia_trabalho(minha_data))
