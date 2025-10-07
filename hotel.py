from typing import List

from customer import Customer
from room import Room
import logging



class Hotel:
    _LOG_FILE = "reservations.log"

    def __init__(self, name: str, rooms: List[Room]) -> None:
        self.name = name
        self.rooms = rooms
        self.booking_log: List[str] = []
        self._setup_logging()

    def _setup_logging(self) -> None:
        logging.basicConfig(
            filename=self._LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def show_available_rooms(self, room_type: str = None) -> List[Room]:
        return [room for room in self.rooms if (room.is_available and room.room_type == room_type)]


    def calculate_total_booking(self, room_number: int, nights) -> float | None:
        room = self.find_room_by_number(room_number)

        if room is None:
            return None

        return room.calculate_price(nights)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights:int) -> bool:
        room = self.find_room_by_number(room_number)

        if room is None:
            return False
        if not room.is_available:
            print(f"Room {room_number} is not available!")
            return False
        if nights <= 0:
            print("Value of nights must be positive!!!")
            return False


        total_price = self.calculate_total_booking(room_number, nights)
        if customer.pay_for_booking(total_price):
            room.book_room()
            customer.add_room(room)
            customer.transactions[room] = total_price
            self.log_booking(customer, room, total_price)
            return True
        else:
            return False

    def log_booking(self, customer: Customer, room: Room, total_price: float) -> None:
        data = f"Customer {customer.name} booked room N{room.room_number} at ${total_price:.2f}"
        self.booking_log.append(data)
        logging.info(data)

    def cancel_booking(self, customer: Customer, room_number: int) -> bool:
        room = self.find_room_by_number(room_number)

        if room is None:
            return False

        if not customer.has_reservation(room):
            print(f"Customer: {customer.name} has no reservation for room N: {room_number}")
            return False

        room.release_room()
        customer.remove_room(room)
        customer.return_money(customer.transactions.pop(room))
        logging.info(f"Customer {customer.name} canceled reservation for {room.room_number}")
        return True

    def find_room_by_number(self, room_number: int) -> Room | None:
        for room in self.rooms:
            if room.room_number == room_number:
                return room

        print(f"Room N: {room_number} does not exist")
        return None