class Flight:
    def __init__(self,flight_no, base_price, total_seats):
        self.flight_no=flight_no
        self.base_price=base_price
        self.total_seats=total_seats


    def display_flight_info(self):
        return (f"Flight No. {self.flight_no} has a base price of {self.base_price} and has a total no. of {self.total_seats} seats")
    


class DomesticFlight(Flight):
    def __init__(self,flight_no, base_price, total_seats,tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent=tax_percent

    def calculate_price(self):
        return self.base_price + (self.base_price * (self.tax_percent / 100))
       

class BookingFlight(DomesticFlight):
    def __init__(self,flight_no, base_price, total_seats,tax_percent):
        super().__init__(flight_no, base_price, total_seats,tax_percent)
        self.booked_seats=0
    
    def check_seat_availability(self,requested_seats):
        avaliable_seats=self.total_seats - self.booked_seats
        if requested_seats<=avaliable_seats:
            print(f"Available seats: {avaliable_seats}")
            return 1
        else:
            print(f"Available seats: {avaliable_seats}. Booking of {requested_seats} seats is not possible")
            return 0
        
    def get_final_price(self,no_of_tickets):
        print(f"Final Price for {no_of_tickets} tickets: {super().calculate_price()*no_of_tickets}")
    
    def book_seats(self,requested_seats):
        if self.check_seat_availability(requested_seats):
            self.booked_seats=self.booked_seats+requested_seats
            print(f"{requested_seats} booked successfully")
            self.get_final_price(requested_seats)
            print(f"Available seats Now:{self.total_seats-self.booked_seats}")

        else:
            print("Booking Failed")

    
    

f = BookingFlight(1234, 2500, 35, 10)

print(f.display_flight_info())

f.book_seats(15)



f.book_seats(5)


f.book_seats(10)


f.book_seats(4)

f.book_seats(6)


