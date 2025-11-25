# Railway Ticket Booking System 
prices = {
    "1st AC": 2800,
    "2nd AC": 1900,
    "3rd AC": 1300,
    "Sleeper": 500
}

print("____Railway Ticket Booking System____\n")

name = input("Enter Passenger Name: ")
age = input("Enter Age: ")
from_station = input("From Station: ")
to_station = input("To Station: ")
train_no = input("Train Number: ")
train_name = input("Train Name: ")

print("\nAvailable Coaches:")
for c in prices:
    print("-", c)

coach = input("\nSelect Coach: ")

if coach in prices:
    fare = prices[coach]

    print("\n----- Ticket Details -----")
    print("Passenger Name:", name)
    print("Age:", age)
    print("From:", from_station)
    print("To:", to_station)
    print("Train No:", train_no)
    print("Train Name:", train_name)
    print("Coach:", coach)
    print("Total Fare: ₹", fare)
    print("\nBooking Successful!! ")

else:
    print("\n#Oops Sorry#\nInvalid coach selected, Please try again.")