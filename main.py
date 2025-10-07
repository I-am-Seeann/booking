import random

from customer import Customer
from hotel import Hotel
from room import Room

ROOM_NUMBERS = 2
ROOM_TYPES = ["Single", "Single", "Double", "Double", "Single"]
ROOM_PRICES = [100, 200, 300, 400, 500]
MAX_GUESTS = [1, 2, 3, 4, 5]

rooms = []
for i in range(ROOM_NUMBERS):
    room = Room(i+1,
                ROOM_TYPES[i],
                random.choice(ROOM_PRICES),
                random.choice(MAX_GUESTS),
                True)
    rooms.append(room)

print("------------------------")
hotel = Hotel("California", rooms)
print(f"Welcome to the Hotel {hotel.name}!")
print("------------------------")

def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Value needs to be an integer")

def get_budget() -> float:
    while True:
        try:
            budget = float(input("Enter your budget: "))
            return budget
        except ValueError:
            print("Budget needs to be a number!")

def belongs_to(room_number: int, customer: Customer) -> bool:
    for room in customer.booked_rooms:
        if room.room_number == room_number:
            return True
    return False

def book_a_room(customer: Customer) -> None:
    print("Booking a room...")
    print("Here are the available rooms:")

    if len(hotel.show_available_rooms()) == 0:
        print("No avalable rooms left")
        return

    for room in hotel.show_available_rooms():
        print("------------------------")
        print(room)
        print("------------------------")

    room_number = get_valid_int("Choose a room by it's NUMBER to book:  ")
    nights = get_valid_int("For how many nights are you going to stay? ")

    if hotel.book_room_for_customer(customer, room_number, nights):
        print(f"Room {room_number} was booked successfully!")

def cancel_a_reservation() -> None:
    print("Canceling a reservation...")
    print("Here are your reservations:")

    if len(customer.booked_rooms) == 0:
        print("No reservations yet.")
        return

    for room in customer.booked_rooms:
        print("------------------------")
        print(room)
        print("------------------------")

    room_number = get_valid_int("Choose a room by it's NUMBER to cancel reservation:  ")

    if belongs_to(room_number, customer):
        hotel.cancel_booking(customer, room_number)
        print(f"Reservation for room N:{room_number} was cancelled successfully!")
    else:
        print(f"Customer {customer.name} does not have a reservation for room N:{room_number}")

# Lets user choose their next move
def get_operation(customer: Customer):
    while True:
        print(f"Current budget is ${customer.budget}")
        print(f"Current score is {customer.score}")

        print("What would you like to do? Enter a number from 1 to 3: ")
        print("1. Book a room")
        print("2. Cancel a reservation")
        print("3. Quit program")

        user_input = input("Please enter your choice: ").strip()
        if user_input == "1":
            book_a_room(customer)
        if user_input == "2":
            cancel_a_reservation()
        if user_input == "3":
            quit()


while True:
    name = input("Enter your name? ")
    budget = get_budget()
    customer = Customer(name, budget)
    operation = get_operation(customer)

