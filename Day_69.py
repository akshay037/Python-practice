# Task number 76 :- Python Program to Get the Class Name of an Instance

class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)

