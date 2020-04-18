class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = False
        self.dead = False

    def run(self):
        self.hungry = True

    def killed(self):
        self.dead = True


justin = Person("Justin", 29)
lucas = Person("Lucas", 29)
zak = Person("Zak", 29)

print(justin.hungry)
justin.run()
print(justin.hungry)
print(lucas.hungry)

