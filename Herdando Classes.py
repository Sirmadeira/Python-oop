#O que e uma subclasse? Ou inheritance?
#Uma subclasse, e basicamente uma mecanica adicional que compartilha os mesmo atributos e metodos, com a a original.
#Inheritance seria, esse fenomeno de compartilhacao

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#Isso daki e uma subclasse que herda da classe employee, basicamente tudo incluindo o seuss metodos
class Developer(Employee):
    raise_amt=1.10
    #Como voce pode ver aqui eu estou sobrepondo a variavel de calsse da employee
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        #Super da a call em relacao a variaveis da classe pai
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):   
        for emp in self.employees:
            print('---->',emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000,'Python')
dev_2 = Developer('Test', 'Employee', 60000,'Java')
print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)
# Para ver oque voce esta fazendo
#print(help(Developer))
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mrg_1=Manager('Sue','Smith',9000,[dev_1])

print(mrg_1.email)
print(mrg_1.remove_emp(dev_2))
print(mrg_1.print_emps())

print(isinstance(mrg_1,Developer))
#Define se e uma instancia, como voce pode ver nao e herdado de developer 
#logo nao e uma instancia de developer, mas sim de  manager