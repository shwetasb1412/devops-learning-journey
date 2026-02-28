class Product():
    def __init__(self):
        self.id=78
        self.name="Amul"
    
    def display(self):
        print(f"ID:{self.id}")
        print(f"Name:{self.name}")

class A(Product):
    def __init__(self):
        super().__init__()
        self.count=50
        self.category="butter"
    
    def display(self):
        super().display()
        print(f"Count:{self.count}")
        print(f"Category: {self.category}")

class B(Product):
    def __init__(self):
        super().__init__()
        self.count=90
        self.category="Milk"
    
    def display(self):
        super().display()
        print(f"Count:{self.count}")
        print(f"Category: {self.category}")

class C(Product):
    def __init__(self):
        super().__init__()
        self.count=56
        self.category="Choco"
    
    def display(self):
        super().display()
        print(f"Count:{self.count}")
        print(f"Category: {self.category}")


a1=A()
b1=B()
c1=C()

a1.display()
b1.display()
c1.display()
    