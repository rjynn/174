class Person:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        
    def say_hello(self):
        print("Hello my name is "+ self.name + " and I am " + str(self.age))
        
def main():
    leo = Person("Leo", 10, "Computing Science")
    leo.say_hello()
    ruby = Person("Ruby", 10, "English")
    ruby.say_hello()
    
main()