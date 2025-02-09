



"Static method cannot access instance variable directly because it is a static method" 

class Example :
    class_variable="I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable=instance_variable
    @staticmethod
    def static_method():
        try:
            print("I am a static method")
        except Exception as e:
            print(e)
            print(Example.class_variable)

    def instance_method(self):
        print(self.instance_variable)
        print(self.class_variable)


obj=Example("I am an instance variable")
obj.static_method()