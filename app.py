class Caluculator:

    def __init__(self, a = 0, b = 20) -> None:
        self.b = b
        self.a = a

    def addition(self) -> int:
        return self.a+self.b
    
    def subtraction(self) -> float:
        return self.a-self.b

cal = Caluculator(a = 3, b = 4)
print(f"Addition : ",cal.addition())
print(f"subtraction : ",cal.subtraction())

# cal1 = Caluculator(a=10, b=5)
# print(f"subtraction : ",cal1.subtraction())