# a = [[1,2,3], 2, 3]
# b = a[0:]
# print(a==b, a is b)

class dog:
    num_of_dogs = 0
    brith_of_dogs = 0

    def bark():
        print("멍") 

    def __init__(self, name, species, brith):
        if brith == 1:
            self.name = name
            self.species = species
            dog.num_of_dogs += 1
            dog.brith_of_dogs += 1
        else:
            dog.num_of_dogs -= 1

    def get_status():
        print(dog.brith_of_dogs)
        print(dog.num_of_dogs)

dog1 = dog('까미', 'sn', 1)
dog2 = dog('가디', 'ws', 1) 
dog3 = dog('제제', 'dh', 1)
dog3 = dog('제제', 'dh', 0)

dog.get_status()
dog.bark()