class Animal():
    living = True

    def __init__(self):
        print("running...")

    def run(self):
        print("Running...")

    def kill(self):
        print("Mardaixa")
        self.living = False


dog = Animal()
print(dog.living)  # Bachirako xa
dog.kill()  # This is how you kill
print(dog.living)  # Marisako


class Person():

    def __init__(self, cname):
        '''Yo chai aafai chalxa'''
        self.name = cname

    def run(self):
        print(self.name, "is running")


awebisam = Person('Awebisam')  # This triggers __init__
awebisam.run()

nerajan = Person("Nirajan")
nerajan.run()
