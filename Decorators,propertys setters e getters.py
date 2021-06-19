class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    #O property decorator existe para vc continuar sendo capaz de utilizar de email como um atributo
    #Ao inves de um metodo
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    #Isso daki e um setter, ele basicamente redefini o fullname tambem como um atributo
    #Possibilitando ao user consinuar usando ele
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname