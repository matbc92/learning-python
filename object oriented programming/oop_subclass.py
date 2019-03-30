# é possivel criar sublasses de classes ja existentes por meio do principio de herança, que eh utilizado pelo comando: class: subclasse(superclasse), o initi de uma super classe não é automaticamente ativado na criação de uma instancia de uma subclasse com init proprio(na ausencia de um init a subclasse herda o o init da superclasse), portanto quando isto é necessario ele deve ser chamado manualmente. Outra proprieade da herança é que uma classe pode herdar multiplas classes em paralelo, e isto afeta a propriedade de acesso aos metodos, que é dada da seguinte forma, quando um metodo é chamado para uma classe
class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
        self.member_phrase = 'Name:"{}" Age:"{}"'.format(name, age)

    def tell(self):
        '''Tell my details.'''
        print (self.member_phrase)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ('(Initialized Teacher: {})'.format(self.name))
        self.teacher_subphrase = 'Salary: "{:d}"'.format(self.salary)
        self.teacher_phrase ="{} {}".format(self.member_phrase,  self.teacher_subphrase)
    def tell(self):
        print (self.teacher_phrase)
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student: {})'.format(self.name))
        self.student_subphrase = 'Marks: "{:d}"'.format(self.marks)
        self.student_phrase = self.member_phrase + self.student_subphrase
    def tell(self):
        print (self.student_phrase)
class Weirdo(Teacher, Student):
    def __init__(self,name, age, marks, salary):
        Teacher.__init__(self,name,age,salary)
        Student.__init__(self,name,age,marks)
        self.weirdo_phrase = '{} {} {}'.format(self.member_phrase ,self.student_subphrase, self.teacher_subphrase)
        print('(Initialized Weirdo: {})'.format(self.name))
    def tell(self):
        print(self.weirdo_phrase)

w = Weirdo('Harry', 30, 85, 20000)
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# prints a blank line
print()
members = [t, s, w]
for member in members:
# Works for both Teachers and Students
    member.tell()

