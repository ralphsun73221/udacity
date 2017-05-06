class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toy):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toy = number_of_toy

#billy_cyrus = Parent("孫", "棕色")
#print(billy_cyrus.last_name)

miley_cyrus = Child("孫", "棕色", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toy)