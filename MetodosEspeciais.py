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
    #Esse metodos sao sempre definido com __ na frente __ atras, sao chamados de dunder.
    #Repr e uma representao nao ambigua do objeto, geralmete utilizado para debuggin loggin etc
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    #E mais utilizado, para algo mais visivel do objeto, geralmente utiulizado para o user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    #Adicianando o salarios dos funcionarios
    def __add__(self, other):
        return self.pay + other.pay
    #Verificando o tamnho dos nomes.
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))