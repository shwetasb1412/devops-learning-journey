flight_no="AI203"
base_fare="4500.75"
tax_percent="5"
seat_numbers="12A,12B,14C,15D"
is_international="True"

final_fare=float(base_fare)+(float(base_fare)*float(tax_percent)/100)
print(f"Final Fare={final_fare}")

seat_numbers_list=seat_numbers.split(",")
print(type(seat_numbers_list))
print(seat_numbers_list)


seat_numbers_set=set(seat_numbers_list)
print(type(seat_numbers_set))


if (is_international=="True"):
        print("is_international:",is_international)
else:
        print("is_international is not boolean")





flight_dict={"flight_no":flight_no,"final_fare":int(final_fare),"seat_numbers":tuple(seat_numbers_list)}
print(type(flight_dict))
print(type(flight_dict["seat_numbers"]))
print("Flight details:",flight_dict)

