from typing import List, Dict

from room import Room


class Customer:
    def __init__(self, name: str, budget: float) -> None:
        if budget < 0:
            raise ValueError("Budget cannot be negative")

        self.name = name
        self.budget = budget
        self.booked_rooms: List[Room] = []
        self.transactions: Dict[Room, float] = {}
        self.score = 0

    def add_room(self, room: Room) -> None:
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if total_price <= 0:
            raise ValueError("Total price should be positive")

        if total_price > self.budget:
            print("Not sufficient budget")
            return False
        else:
            self.budget -= total_price
            self.score += total_price * 100
            return True

    def has_reservation(self, room: Room) -> bool:
        return room in self.booked_rooms

    def return_money(self, amount: float) -> None:
        self.budget += amount
        self.score -= amount * 100

    def show_booking_summary(self) -> str:
        return "".join([f"Room N: {room.room_number}\tPrice: ${room.price_per_night}" for room in self.booked_rooms])


