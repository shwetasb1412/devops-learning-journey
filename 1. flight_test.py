class Flight():
    def __init__(self,flight_no, source, destination, base_fare):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.base_fare=base_fare

    def get_flight_info(self):
        print(f"Flight No: {self.flight_no}, Source: {self.source}, Destination: {self.destination}")

    
    
    def calculate_fare(self,count,discount_percent=0):
        print(f"Total fare of {count} person with {discount_percent}% disocunt:{(self.base_fare -(self.base_fare*discount_percent/100))*count}")

    

    def update_route(self, destination,source=None):
        self.source=source
        self.destination=destination
       

    


f=Flight("A111","Texas","Hawai",8000.0)
f.get_flight_info()
f.calculate_fare(5)
f.calculate_fare(10,10)
f.update_route("Milan")
f.get_flight_info()
f.update_route("Hawai","Tennessee")
f.get_flight_info()
