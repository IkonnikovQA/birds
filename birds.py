class Bird:
    wings = True
    beak = True
    plumage = True

    def fly(self):
        print('I flap my wings')

    def walk(self):
        pass

class Sparrow(Bird):
    size = 'small'

    def walk(self):
        print('jump')


class Duck(Bird):
    def walk(self):
        print('step')


chizhik = Sparrow()
pyzhik = Sparrow()
duck = Duck()
chizhik.size = 'medium'

print(chizhik.size)
print(pyzhik.size)
chizhik.walk()
print(chizhik.wings)
chizhik.fly()
duck.walk()

