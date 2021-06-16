class Trabalhador:
#Variaveis de classe, sao compartilhadas por todas as instancias
	num_of_emps=0
	aumento_salario=1.04

	def __init__(self,nome,sobrenome,salario):# Self e convencao
		self.nome=nome
		#Isso daki e um atributo 
		self.sobrenome= sobrenome
		self.salario = salario
		self.email= nome+'.'+sobrenome+'@gmail.com'

		Trabalhador.num_of_emps+=1
		#Nesse caso por exemplo, eu n preciso altera isso logo ja do call diretamente em Trabalhador, porque todas as instancias vao ser assim
	#pass #- Quebra a classe
	# Instancias sao partes de uma classe, cada trabalhador criado e uma instancia. O que cria e a classe.
	def nomecompleto(self):
		return f'Nome completo {self.nome} {self.sobrenome}'
	def acrescentar_salario(self):
		self.salario =int(self.salario * self.aumento_salario)
		#Self.aumento_salario e melhor do que Trabalhador.aumento_salaro porque caso eu queira mudar uma instancia de um especifico como emp1 eu consigo
	#Isso daki e um metodos


trab_1=Trabalhador('Jose','Antonio',50000)#Exemplo de instancia
trab_2=Trabalhador('Antonio','Batata',6000)


print(trab_1.email)

print(trab_2.email)#Atributos nao precisam de parantese

print(trab_1.salario)
trab_1.acrescentar_salario()
print(trab_1.salario)

print(trab_1.nomecompleto()) #Metodos precisam de parenteses)
#No caso acima nao
print(Trabalhador.nomecompleto(trab_1))
#Nesse caso precisa passar a instancia pq nao identifica qm seria o self
print(trab_1.__dict__)
#Dict faz um dicionario com todos os atributos definido

print(Trabalhador.num_of_emps)