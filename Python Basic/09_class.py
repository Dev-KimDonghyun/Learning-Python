# 2025.08.20
# 09_class.py

class Person :

    # 생성자(Constructor)
    def __init__ (self, name, age) :
        self.name = name
        self.age = age

    # 메서드(Method)
    def shokai(self) :
        return f'My name is {self.name}, and I am {self.age} years old.'


hito_1 = Person("Donghyun", 19)
hito_2 = Person("Takahashi", 22)

print(hito_1.shokai())
print(hito_2.shokai())